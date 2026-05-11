import requests
import time

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

URL = "https://quotes.toscrape.com/"


def crawl(delay=6):

    to_visit = [URL]
    visited = set()
    pages = []

    while to_visit:

        current_URL = to_visit.pop(0)

        #Stops from jumping to subsections of the same URL
        #REFERANCE: AI gave ideas on who to achiive this
        #https://chatgpt.com/share/6a02228b-e95c-8394-9447-984c89d4a371
        current_URL = urldefrag(current_URL)[0]

        #Prevents the same page being crawled twice
        if current_URL in visited:
            continue

        print(f"Crawling: {current_URL}")

        #HTTP request
        answer = requests.get(current_URL)

        #Parse HTML
        #REFERENCE: Use of BeautifulSoup 
        #Crummy.com. (2020). Beautiful Soup Documentation — Beautiful Soup 4.14.3 documentation. [online] Available at: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ [Accessed 07 May 2026]

        soup = BeautifulSoup(answer.text, "html.parser")
        page_text = soup.get_text(separator=" ")

        pages.append({
            "url": current_URL,
            "text": page_text
        })

        visited.add(current_URL)

        #Finds all links on the current page
        links = soup.find_all("a")


        #REFERENCE: AI used to code how to avoid crawling already visited pages
        #https://chatgpt.com/share/6a0223a1-d4f8-8397-9e8b-a5dbd2d0488d
        for link in links:

            href = link.get("href")

            if href:

                #Build another full URL
                new_URL = urljoin(current_URL, href)

                #Removes any # fragments
                new_URL = urldefrag(new_URL)[0]

                #Only crawl pages inside the quotes website
                if new_URL.startswith(URL):

                    #Only add pages that have not been visited
                    if new_URL not in visited and new_URL not in to_visit:
                        to_visit.append(new_URL)

        #Politeness window
        if to_visit:
            time.sleep(delay)

    return pages


if __name__ == "__main__":
    pages = crawl()
    print(f"Crawled {len(pages)} pages.")



