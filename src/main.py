from crawler import crawl
from indexer import create_index, add_page_to_index, save_index, load_index
from search import print_word, find_words

file = "data/index.json"

#REFERENCE: AI used to help build the index file 
#https://chatgpt.com/share/6a02272f-2d24-83eb-a635-e60368eab201
def build():
    #Creats empty index
    index = create_index()

    pages = crawl()

    for page in pages:
        #For every page; extrac words, count frequencies, stroe positions, add to inverted index
        add_page_to_index(index, page["url"], page["text"])

    save_index(index, file)

#REFERENCE: AI help me find a very basic structure on how some logic might work
#https://chatgpt.com/share/6a02284d-1df4-83eb-8b40-fd89374fff3b
def main():

    index = None

    while True:

        #Gets the users command and removes spaces
        command = input(">").strip().split()

        #Makes sure something was entered
        if not command:
            continue

        #Inverted index, if build is types it runs the crawler and then created the inverted index
        if command[0] == "build":

            build()

        #Loads the saved index file means searching is now possible
        elif command[0] == "load":

            index = load_index(file)

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

            #index has been loaded?
            if index is None:
                continue

            #Entered search terms
            if len(command) < 2:
                continue

            results = find_words(index, command[1:])

            #Checks if any matching pages were found
            if results:

                print("Pages found are:")

                for page in results:
                    print(page)

            else:
                print("No pages found.")

        #Exits the program
        elif command[0] == "exit":
            break

        else:
            print("No Knowm Command ")


if __name__ == "__main__":
    main()