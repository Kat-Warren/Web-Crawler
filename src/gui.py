import tkinter as tk
from indexer import load_index
from search import find_words

INDEX_FILE = "data/index.json"

#REFERENCE: AI was used to code this GUI since no major logic was used it was mostly astetics 
#https://chatgpt.com/share/6a022406-c408-838a-bf6b-df534ae9c02f


def run_search():
    query = search_box.get()

    results_area.delete("1.0", tk.END)

    #Checks the user has entered anything
    if not query.strip():
        results_area.insert(tk.END, "Enter a search term")
        return

    #Splits the search into separate words
    words = query.split()
    results = find_words(index, words)

    #Displays the matching pages if any were found
    if results:
        results_area.insert(tk.END, "Search Results:\n\n")

        for number, page in enumerate(results, start=1):
            results_area.insert(tk.END, f"{number}. {page}\n")
    else:
        results_area.insert(tk.END, "No pages found")


#REFERENCE: This code focousing on the looks of the page was written by chat GPT
#https://chatgpt.com/share/6a022406-c408-838a-bf6b-df534ae9c02f
index = load_index(INDEX_FILE)

window = tk.Tk()
window.title("Moogle")
window.geometry("600x400")

title = tk.Label(window, text="Moogle", font=("Arial", 18))
title.pack(pady=10)

search_box = tk.Entry(window, width=60)
search_box.pack(pady=5)

search_button = tk.Button(window, text="Search", command=run_search)
search_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady=5)

results_area = tk.Text(window, width=70, height=15)
results_area.pack(pady=10)

window.mainloop()