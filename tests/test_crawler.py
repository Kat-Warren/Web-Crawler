from src.crawler import crawl


#Runs the crawler once for all tests
pages = crawl(delay=0)


#Checks the crawler returns a list
def test_crawl_returns_list():
    assert isinstance(pages, list)


#Checks that at least one page was found
def test_crawl_finds_pages():
    assert len(pages) > 0


#Checks each page has a URL and text
def test_url_and_text():
    first_page = pages[0]
    assert "url" in first_page
    assert "text" in first_page


#Checks the first page is the website homepage
def test_homepage():
    first_page = pages[0]
    assert first_page["url"] == "https://quotes.toscrape.com/"


#Checks the crawler finds tag pages
def test_tag_pages():
    urls = [page["url"] for page in pages]
    assert any("/tag/" in url for url in urls)


#Checks the crawler finds author pages
def test_author_pages():
    urls = [page["url"] for page in pages]
    assert any("/author/" in url for url in urls)


#Checks that the text is not empty
def test_crawl_gets_page_text():
    first_page = pages[0]
    assert len(first_page["text"]) > 0


#Checks the crawler does not crawl the same page twice
def test_duplicate_pages():
    urls = [page["url"] for page in pages]
    assert len(urls) == len(set(urls))