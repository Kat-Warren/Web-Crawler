import re
import json
from collections import defaultdict

#REFERANCE: AI used to help wirte the default dict code
#https://chatgpt.com/share/69ff5beb-68e4-83eb-a2b4-50f1163d387e

def create_index():
     #Create the inverted index structure
     #AI helped create this 
     return defaultdict(
        lambda: defaultdict(
            lambda: {
                "frequency": 0,
                "positions": []
            }
        )
    )

def clean(text):
    text = text.lower()
    words = re.findall(r"\b[a-zA-Z]+\b", text)
    return words



def add_page_to_index(index, url, text):
    words = clean(text)

    for position, word in enumerate(words):
        index[word][url]["frequency"] += 1
        index[word][url]["positions"].append(position)

    return index


def convert_to_normal_dict(index):
    #Save it into normal dictionary so it can be saved as JASON
    return {
        word: {
            url: data
            for url, data in pages.items()
        }
        for word, pages in index.items()
    }


def save_index(index, filename):
    
    normal_index = convert_to_normal_dict(index)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(normal_index, file, indent=4)


def load_index(filename):
    
    #Loading the index from a JSON file.
    
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    index = create_index()

    add_page_to_index(
        index,
        "https://quotes.toscrape.com/page/1/",
        "Good friends, good books, and good ideas."
    )

    print(convert_to_normal_dict(index))

