# News Headlines Scraper

A simple Python script that fetches news headlines from websites and saves them to a text file.

## Project Structure

```
news-scraper/
├── scraper.py          # Main script
├── requirements.txt    # Dependencies
├── headlines.txt       # Output file (generated after running)
└── README.md          # This file
```

## Installation

First, install the required libraries:

```
pip install requests beautifulsoup4
```

## How to Run

Open terminal in the project folder and run:

```
python scraper.py
```

You'll see a menu with news sources:
```
News Scraper

Choose source:
1. Hacker News
2. The Guardian
3. TechCrunch
4. Custom URL

Enter choice:
```

Type a number (1-4) and press Enter. The script will fetch headlines and save them to `headlines.txt`.

## What the Code Does

The `scraper.py` file has three main functions:

**1. get_headlines(url)** - This function takes a URL, sends a request to fetch the webpage, and uses BeautifulSoup to parse the HTML. It looks for headline tags (like h1, h2, h3) and extracts the text from them. For Hacker News specifically, it targets the special class they use for titles. It removes any duplicates and returns up to 25 unique headlines.

**2. save_to_file(headlines)** - Takes the list of headlines and writes them to a file called `headlines.txt`. It adds a timestamp at the top, numbers each headline, and shows the total count at the bottom.

**3. main()** - This is what runs when you start the program. It shows you a menu of news sources, asks you to pick one, fetches the headlines from that source, displays the first 5 in the terminal, and saves all of them to the text file.

The script uses the `requests` library to fetch web pages and `BeautifulSoup` to parse the HTML and find headlines. It includes basic error handling so it won't crash if something goes wrong.

## Example Output

After running, `headlines.txt` will look like:

```
News Headlines - 2025-11-17 15:30
============================================================

1. New AI Model Breaks Performance Records
2. Climate Summit Reaches Historic Agreement
3. Tech Company Announces Major Product Launch
...
============================================================
Total: 25 headlines
```

## Notes

- Some websites may block scraping attempts
- Results depend on the website's structure
- Headlines are saved with timestamp for reference
- The script only scrapes publicly available content