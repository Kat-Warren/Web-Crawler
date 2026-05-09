from crawler import crawl
from indexer import create_index, add_page_to_index, save_index, load_index
from search import print_word, find_words

INDEX_FILE = "data/index.json"


def build():
    index = create_index()

    pages = crawl()

    for page in pages:
        add_page_to_index(index, page["url"], page["text"])

    save_index(index, INDEX_FILE)

    print("Index built and saved to data/index.json")

def main():

    index = None

    while True:

        #Gets the users command
        command = input(">").strip().split()

        #Makes sure something was entered
        if not command:
            continue

        #Builds the inverted index
        if command[0] == "build":

            build()

        #Loads the saved index file
        elif command[0] == "load":

            index = load_index(INDEX_FILE)

            print("Index loaded")

        #Prints the inverted index for a single word
        elif command[0] == "print":

            #Checks if the index has been loaded
            if index is None:
                print("Load the index first")
                continue

            #Checks the user entered a word
            if len(command) < 2:
                print("Usage: print <word>")
                continue

            print_word(index, command[1])

        #Finds pages containing search words
        elif command[0] == "find":

            #Checks if the index has been loaded
            if index is None:
                print("Load the index first")
                continue

            #Checks the user entered search terms
            if len(command) < 2:
                print("Usage: find <words>")
                continue

            results = find_words(index, command[1:])

            #Checks if any matching pages were found
            if results:

                print("Pages found:")

                for page in results:
                    print(page)

            else:
                print("No pages found")

        #Exits the program
        elif command[0] == "exit":
            break

        else:
            print("Unknown command")


if __name__ == "__main__":
    main()