import json


def print_word(index, word):

    #Search not case senstative 
    word = word.lower()

    #Checks if the word exists in the index
    if word in index:
        #Stops the one-line dictionry
        print(json.dumps(index[word], indent = 3))

    else:
        print("Word not found")



#Logic was written entiraly by me 
def find_words(index, words):

    lowercase_words = []
    for word in words:

        lowercase_words.append(word.lower())

    matching_pages = None

    #Loops through every search word
    for word in lowercase_words:

        #Checks if the word exists in the index
        if word not in index:
            return []

        #Gets all pages containing the current word
        current_pages = set(index[word].keys())

        #Checks if this is the first word
        if matching_pages is None:

            #Stores the pages from the first word
            matching_pages = current_pages

        else:

            #Keeps only the pages that appear in both sets
            matching_pages = matching_pages.intersection(current_pages)

    results = list(matching_pages)

    #Returns the matching pages
    return results