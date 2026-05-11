# Web Crawler Search Engine

## Overview

This project is a Python-based web crawler and search engine. It crawls the website:

https://quotes.toscrape.com/


## Features

- Crawls the full website
- Creates an inverted index
- Stores:
  - Word frequency
  - Word positions
  - Page URLs
- Saves the index into a JSON file
- Searches for single or multiple words
- GUI search window using Tkinter
- Automated tests using Pytest

---

## Project Structure
As dentoted by the guidance, only adding the gui file
```text
Web-Crawler/
│
├── src/
│   ├── __init__.py
│   ├── crawler.py
│   ├── indexer.py
│   ├── search.py
│   ├── main.py
│   └── gui.py
│
├── tests/
│   ├── __init__.py
│   ├── test_crawler.py
│   ├── test_indexer.py
│   └── test_search.py
│
├── data/
│   └── index.json
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- JSON
- Tkinter
- Pytest

---

## Installation

### Open the project folder

```bash
cd Web-Crawler
```

### Open a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

```bash
venv\Scripts\activate
```


### Install requirments

```bash
pip install -r requirements.txt
```

---

## Running the Search Engine

```bash
python src/main.py
```

---

## Commands
### Build the index
Crawls the website and inverted idex

```text
build
```
### Load the index
Loads JSON file
```text
load
```

### Prints the inverted index
Prints the inverted index for a single word

```text
print cat
```

### Search for word

```text
find cat
```

### Exit the program

```text
exit
```

---

## Running the GUI

```bash
python src/gui.py
```

---

## Running Tests

```bash
python -m pytest
```

---


## How the Inverted Index Works

The inverted index stores words as keys and links them to pages containing those words.


---

## Author

Katherina Warren