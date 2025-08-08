import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    """Scrape the quotes from the given url"""
    try:
        response = requests.get(url)
        response.raise_for_status()     # raises an HTTPError for bad responses
        html = response.text

        # parse html
        soup = BeautifulSoup(html, "html.parser")

        # extract authors and quotes
        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        print(f"Found {len(quotes)} quotes \n")

        for quote, author in zip(quotes, authors):
            print(f'"{quote.text}" - {author.text}')
            print("-" * 50)

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error has occured: {e}")

if __name__ == "__main__":
    url = "http://quotes.toscrape.com/"
    scrape_quotes(url)
