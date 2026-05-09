import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


URL = "https://quotes.toscrape.com/"

def crawl():
    
    current_URL = URL
    pages = []

    while current_URL:
        print(f"Crawling:{current_URL}")
        #The HTTP request
        answer = requests.get(current_URL)

        #Parse HTML
        soup = BeautifulSoup(answer.text, "html.parser")

        page_text = soup.get_text(separator=" ")

        pages.append({
            "url": current_URL,
            "text": page_text
        })

        #Find the next button
        #REFERANCE: AI helped me find this method to use the next button

        next = soup.select_one("li.next a")

        if next:
            #Build another URL 
            current_URL = urljoin(current_URL, next["href"])

            #The politness window
            time.sleep(6)
        else:
            current_URL = None
        
    return pages


if __name__ == "__main__":
    pages = crawl()
    print(f"Crawled {len(pages)} pages.")



















