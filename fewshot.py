import json
import os
import pandas as pd


class FewShotPosts:
    def __init__(self, file_path=None):
        if file_path is None:
            file_path = os.path.join("data", "processed_post.json")
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path=None):
        if file_path is None:
            file_path = os.path.join("data", "processed_post.json")
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df["length"] = self.df["line_count"].apply(self.categorise_length)
            all_tags = self.df["tags"].apply(lambda x: x).sum()
            self.unique_tags = set(list(all_tags))

    @staticmethod
    def categorise_length(line_count):
        if line_count <= 10:
            return "short"
        elif 10 < line_count <= 20:
            return "medium"
        else:
            return "long"

    def get_tags(self):
        return sorted(list(self.unique_tags))

    def get_filtered_posts(self, length, language, tag):
        return self.df[
            (self.df["language"] == language)
            & (self.df["length"] == length)
            & (self.df["tags"].apply(lambda tags: tag in tags))
        ].to_dict(orient="records")


if __name__ == "__main__":
    fs = FewShotPosts()
    print(fs.get_filtered_posts("short", "English", "Java"))