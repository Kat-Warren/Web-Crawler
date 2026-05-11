import re
import json
from collections import defaultdict

#REFERANCE: AI used to help wirte the default dict code
#https://chatgpt.com/share/69ff5beb-68e4-83eb-a2b4-50f1163d387e

#REFERENCE: AI was also used to generate what functions should be added 
#https://chatgpt.com/share/6a0225ba-06d0-83eb-9f04-1924038ac14d


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

#REFERENCE: AI used to easly clean the text
#https://chatgpt.com/share/6a022601-04dc-83eb-a24e-ce84aad303d2
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
        #Loops through all words
        word: {
             #Loops through all pages finding that word
            url: data
            for url, data in pages.items()
        }
        for word, pages in index.items()
    }


def save_index(index, filename):
    
    normal_index = convert_to_normal_dict(index)
    #Gets the index from a JSON file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(normal_index, file, indent=4)


def load_index(filename):
    
    #Loading the index from a JSON file.
    
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


