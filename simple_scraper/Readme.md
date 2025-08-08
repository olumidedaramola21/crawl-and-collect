# Simple Web Scraper

A Python web scraper that extracts quotes and authors from [Quotes to Scrape](http://quotes.toscrape.com/) website using BeautifulSoup and requests.

## Features

- Scrapes quotes and their authors from quotes.toscrape.com
- Handles HTTP errors gracefully with proper exception handling
- Clean, formatted output with quote text and author attribution
- Simple and easy-to-understand code structure

## Requirements

- Python 3.6+
- requests
- beautifulsoup4

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd simple_scraper
   ```
3. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

Run the script directly:

```bash
python main.py
```

The script will:
1. Fetch the webpage from quotes.toscrape.com
2. Parse the HTML content
3. Extract all quotes and their authors
4. Display them in a formatted output

## Example Output

```
Found 10 quotes 

"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking." - Albert Einstein
--------------------------------------------------
"It is our choices, Harry, that show what we truly are, far more than our abilities." - J.K. Rowling
--------------------------------------------------
...
```

## Code Structure

- `scrape_quotes(url)`: Main function that handles the web scraping process
  - Sends HTTP GET request to the target URL
  - Parses HTML using BeautifulSoup
  - Extracts quote text and author information
  - Handles exceptions for network and parsing errors

## Error Handling

The script includes comprehensive error handling:
- **RequestException**: Catches network-related errors (connection issues, timeouts, etc.)
- **HTTPError**: Automatically raised for HTTP error status codes (4xx, 5xx)
- **General Exception**: Catches any other unexpected errors during execution

## Customization

You can easily modify the script to:
- Scrape different websites by changing the `url` variable
- Extract different HTML elements by modifying the CSS selectors
- Add data export functionality (CSV, JSON, etc.)
- Implement pagination support for multi-page scraping

## License

This project is open source and available under the [MIT License](LICENSE).

