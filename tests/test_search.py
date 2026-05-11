from src.search import find_words


#Ssingle word 
def test_single_word_search():
    index = {
        "cat": {
            "page1": {}
        }}
    results = find_words(index, ["cat"])
    assert "page1" in results


#Multiple words 
def test_multiple_word_search():
    index = {
        "cat": {
            "page1": {},
            "page2": {}},
        "dog": {
            "page1": {}}}
    results = find_words(index, ["cat", "dog"])
    assert results == ["page1"]


#Missing words return an empty list
def test_missing_word():
    index = {
        "cat": {
            "page1": {}
        }
    }
    results = find_words(index, ["dog"])
    assert results == []


#Search is not case sensitive
def test_case_insensitive_search():
    index = {
        "cat": {
            "page1": {}}}
    results = find_words(index, ["CAT"])
    assert "page1" in results


#Pages must contain all words
def test_search():
    index = {
        "cat": {
            "page1": {},
            "page2": {}},
        "mat": {
            "page2": {} }}
    results = find_words(index, ["cat", "mat"])
    assert results == ["page2"]


#Empty searches return an empty list
def test_empty():
    index = {}
    results = find_words(index, ["cat"])
    assert results == []

#Repeated search words still work
def test_repeated_search_word():
    index = {
        "cat": {
            "page1": {}
        }}
    results = find_words(index, ["cat", "cat"])
    assert "page1" in results


#Two or more words
def test_three_word_search():

    index = {
        "cat": {
            "page1": {},
            "page2": {} },
        "sat": {
            "page1": {} },
        "mat": {
            "page1": {}}}

    results = find_words(index, ["cat", "sat", "mat"])
    assert results == ["page1"]


#A word with multiple pages returns all pages
def test_word_with_multiple_pages():

    index = {
        "cat": {
            "page1": {},
            "page2": {},
            "page3": {}
        }}
    results = find_words(index, ["cat"])
    assert "page1" in results
    assert "page2" in results
    assert "page3" in results