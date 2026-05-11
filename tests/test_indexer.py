from src.indexer import create_index, clean, add_page_to_index


#index is created as a dictionary
def test_create_index():
    index = create_index()
    assert isinstance(index, dict)


#Converted to lowercase
def test_lowercase():
    words = clean("HELLO World")
    assert words == ["hello", "world"]


#added into the index
def test_page_to_index():
    index = create_index()
    add_page_to_index(
        index,
        "page1",
        "find the cats mat"
    )
    assert "cats" in index


#Frequency is correct
def test_frequency():
    index = create_index()
    add_page_to_index(
        index,
        "page1",
        "find the cats mat"
    )

    assert index["cats"]["page1"]["frequency"] == 1


#Positions are correct
def test_word_positions():
    index = create_index()
    add_page_to_index(
        index,
        "page1",
        "find the cats mat"
    )

    assert index["cats"]["page1"]["positions"] == [2]


#Different words are stored
def test_multiplewords():
    index = create_index()
    add_page_to_index(
        index,
        "page1",
        "find the cats mat"
    )
    assert "find" in index
    assert "mat" in index


#Repeated words are counted correctly
def test_repeated_words():
    index = create_index()
    add_page_to_index(
        index,
        "page1",
        "cat cat cat"
    )
    assert index["cat"]["page1"]["frequency"] == 3

#Words from different pages are stored togther
def test_multiple_pages():
    index = create_index()
    add_page_to_index(
        index,
        "page1",
        "cat")
    add_page_to_index(
        index,
        "page2",
        "cat" )
    assert "page1" in index["cat"]
    assert "page2" in index["cat"]