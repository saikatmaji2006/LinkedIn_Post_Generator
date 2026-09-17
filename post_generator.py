from model import llm
from fewshot import FewShotPosts

fs = FewShotPosts()


def get_length_str(length):
    """Convert length category to a human-readable line range."""
    if length == "short":
        return "1 to 5 lines"
    if length == "medium":
        return "6 to 10 lines"
    if length == "long":
        return "11 to 15 lines"


def generate_post(length, language, topic):
    """Generate a LinkedIn post using the LLM with few-shot examples."""
    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {topic}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English.
    The script for the generated post should always be English.
    '''
    examples = fs.get_filtered_posts(length, language, topic)
    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."
        for i, e in enumerate(examples):
            prompt += f"\n\n Example {i} \n\n {e['Text']}"
            if i == 1:
                break

    else:
        ex = fs.get_filtered_posts("medium","English","System Design")
        #print(ex)
        for i,e in enumerate(ex):
            prompt += f"4) Use the writing style as per the following examples.\n\n Example {i} \n\n {e['Text']}"
            if i==1:
                break


    response = llm.invoke(prompt)
    #print(prompt)
    return response.content
