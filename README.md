# Crawl and Collect 🕷️

A  collection of web scrapers using different techniques and libraries in Python. This repository will demonstrate various approaches to web scraping, from simple HTML parsing to advanced techniques for handling dynamic content.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## 🎯 Overview

This repository serves as a learning resource and reference for different web scraping methodologies. Each project demonstrates specific techniques, challenges, and solutions commonly encountered in web scraping.



## 📁 Projects

### 1. Simple Scraper (`simple_scraper/`)
- **Technique**: BeautifulSoup + requests
- **Target**: Static HTML content
- **Libraries**: `beautifulsoup4`, `requests`
- **Features**: Basic HTML parsing, CSS selectors


### 3. Weather Scraper (`weather_scraper/`)
- **Technique**: OpenWeatherMap API
- **Target**: Weather data 
- **Libraries**: `requests`, `json`, `pandas`




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



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



