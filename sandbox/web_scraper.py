import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://quotes.toscrape.com/"
current_url = base_url
page_number = 1

while current_url:
    print(f"\n--- Scraping Page {page_number}: {current_url} ---")
    
    # 1. Fetch the page and check for HTTP errors
    response = requests.get(current_url)
    response.raise_for_status()  # Raises an HTTPError if the status is 4xx or 5xx
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 2. Extract all quotes on the page
    for quote_div in soup.find_all("div", class_="quote"):
        quote_text = quote_div.find("span", class_="text").get_text(strip=True)
        author = quote_div.find("small", class_="author").get_text(strip=True)
        print(f"{quote_text} — {author}")
    
    # 3. Locate the 'next' link to continue or stop the loop
    next_li = soup.find("li", class_="next")
    if next_li:
        next_href = next_li.find("a")["href"]
        current_url = urljoin(base_url, next_href)
        page_number += 1
    else:
        print("\nReached the last page. Scraping complete!")
        current_url = None