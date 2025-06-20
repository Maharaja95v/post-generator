import pandas as pd
import json
import os 


class FewShotPosts:
    def __init__(self, file_path=None):
        if file_path is None:
            base_path = os.path.dirname(__file__)  # path of few_shot.py
            file_path = os.path.join(base_path, "data", "processed_posts.json")
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            # collect unique tags
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &  # Tags contain 'Influencer'
            (self.df['language'] == language) &  # Language is 'English'
            (self.df['length'] == length)  # Line count is less than 5
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        if self.unique_tags is not None:
            return self.unique_tags
        return []


if __name__ == "__main__":
    fs = FewShotPosts()
    # print(fs.get_tags())
    posts = fs.get_filtered_posts("Medium","Hinglish","Job Search")
    print(posts)
