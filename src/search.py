import json


def print_word(index, word):

    #Makes the search not case sensitive
    word = word.lower()

    #Checks if the word exists in the index
    if word in index:

        #Prints the inverted index for the word
        print(json.dumps(index[word], indent = 4))

    else:
        print("Word not found")


def find_words(index, words):

    #Converts all words to lowercase
    words = [word.lower() for word in words]

    matching_pages = None

    #Loops through all search words
    for word in words:

        #Checks if the word exists in the index
        if word not in index:
            return []

        #Gets all pages containing the word
        pages = set(index[word].keys())

        #First search word
        if matching_pages is None:
            matching_pages = pages

        else:
            #Finds pages containing all words
            matching_pages = matching_pages.intersection(pages)

    #Returns the matching pages as a list
    return list(matching_pages)