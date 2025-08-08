# Crawl and Collect 🕷️

A  collection of web scrapers using different techniques and libraries in Python. This repository will demonstrate various approaches to web scraping, from simple HTML parsing to advanced techniques for handling dynamic content.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Installation](#installation)
- [Usage](#usage)
- [Libraries Used](#libraries-used)
- [License](#license)


## 🎯 Overview

This repository serves as a learning resource and reference for different web scraping methodologies. Each project demonstrates specific techniques, challenges, and solutions commonly encountered in web scraping.



## 📁 Projects

### 1. Simple Scraper (`simple_scraper/`)
- **Technique**: BeautifulSoup + requests
- **Target**: Static HTML content
- **Libraries**: `beautifulsoup4`, `requests`
- **Features**: Basic HTML parsing, CSS selectors

### 2. Dynamic Content Scraper (Coming Soon)
- **Technique**: Selenium WebDriver
- **Target**: JavaScript-heavy websites
- **Libraries**: `selenium`, `webdriver-manager`
- **Features**: Browser automation, waiting for elements

### 3. Weather Scraper (`weather_scraper/`)
- **Technique**: OpenWeatherMap API
- **Target**: Weather data for ML projects
- **Libraries**: `requests`, `json`, `pandas`

### 4. API Scraper (Coming Soon)
- **Technique**: Direct API calls
- **Target**: REST/GraphQL APIs
- **Libraries**: `requests`, `json`
- **Features**: Authentication, pagination, rate limiting



## 💻 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/olumidedaramola21/crawl-and-collect.git
   cd crawl-and-collect
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

## 🚀 Usage

Each scraper project has its own directory with specific instructions:

```bash
# Navigate to a specific scraper
cd simple_scraper/

# Run the scraper
python main.py
```

## 📚 Libraries Used

| Library | Purpose | Use Case |
|---------|---------|----------|
| `beautifulsoup4` | HTML/XML parsing | Static content extraction |
| `requests` | HTTP requests | API calls, page fetching |
| `pandas` | Data manipulation | Data cleaning, analysis, CSV export |
| `selenium` | Browser automation | JavaScript-heavy sites |
| `scrapy` | Scraping framework | Large-scale scraping projects |



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



