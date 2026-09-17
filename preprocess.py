import json
import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from model import llm


def processed_posts(raw_file_path=None, processed_file_path=None):
    """Read raw LinkedIn posts, enrich with metadata, unify tags, and save."""
    if raw_file_path is None:
        raw_file_path = os.path.join("data", "raw_data.json")
    if processed_file_path is None:
        processed_file_path = os.path.join("data", "processed_post.json")

    enriched_post = []
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post["Text"])
            x = post | metadata
            enriched_post.append(x)

    unified_tags = get_unified_tags(enriched_post)

    for i in enriched_post:
        old_tag = i["tags"]
        new_tag = {unified_tags[x] for x in old_tag}
        i["tags"] = list(new_tag)

    with open(processed_file_path, encoding="utf-8", mode="w") as outfile:
        json.dump(enriched_post, outfile, indent=4)

    print(enriched_post)


def get_unified_tags(posts):
    """Use LLM to merge similar tags into a shorter unified list."""
    unique_tags = set()
    for i in posts:
        unique_tags.update(i["tags"])

    template = '''
        I will give you a list of tags. You need to unify tags with the following requirements,
        1. Tags are unified and merged to create a shorter list.
        Example 1: "Jobseekers", "Job Hunting" can be all merged into a single tag "Job Search".
        Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
        Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
        Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
        2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
        3. Output should be a JSON object, No preamble
        3. Output should have mapping of original tag and the unified tag.
        For example: {{"Jobseekers": "Job Search", "Job Hunting": "Job Search", "Motivation": "Motivation"}}

        Here is the list of tags:
        {tags}
        '''

    pt = PromptTemplate.from_template(template)
    json_parser = JsonOutputParser()
    chain = pt | llm | json_parser
    try:
        res = chain.invoke(input={"tags": unique_tags})
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse tags.")

    print(res)
    return res


def extract_metadata(post):
    """Extract line count, language, and tags from a single LinkedIn post."""
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble.|
    2. JSON object should have exactly three keys: line_count, language and tags.
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish (Hinglish means hindi + english)

    Here is the actual post on which you need to perform this task:
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    json_parser = JsonOutputParser()
    chain = pt | llm | json_parser

    try:
        res = chain.invoke(input={"post": post})
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse post.")
    return res


if __name__ == "__main__":
    processed_posts()
