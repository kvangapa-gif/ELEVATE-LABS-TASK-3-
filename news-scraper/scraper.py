import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_headlines(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        headlines = []
        
        if 'ycombinator' in url:
            for item in soup.find_all('span', class_='titleline'):
                link = item.find('a')
                if link:
                    headlines.append(link.text.strip())
        else:
            for tag in soup.find_all(['h1', 'h2', 'h3']):
                text = tag.text.strip()
                if len(text) > 15 and len(text) < 150:
                    headlines.append(text)
        
        return list(dict.fromkeys(headlines))[:25]
    
    except Exception as e:
        print(f"Error: {e}")
        return []

def save_to_file(headlines):
    with open('headlines.txt', 'w', encoding='utf-8') as f:
        f.write(f"News Headlines - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("="*60 + "\n\n")
        for i, headline in enumerate(headlines, 1):
            f.write(f"{i}. {headline}\n")
        f.write(f"\n{'='*60}\nTotal: {len(headlines)} headlines\n")
    print(f"Saved {len(headlines)} headlines to headlines.txt")

def main():
    print("News Scraper\n")
    
    sources = {
        '1': 'https://news.ycombinator.com/',
        '2': 'https://www.theguardian.com/international',
        '3': 'https://techcrunch.com'
    }
    
    print("Choose source:")
    print("1. Hacker News")
    print("2. The Guardian")
    print("3. TechCrunch")
    print("4. Custom URL\n")
    
    choice = input("Enter choice: ")
    
    if choice == '4':
        url = input("Enter URL: ")
    else:
        url = sources.get(choice, sources['1'])
    
    print(f"\nFetching from {url}...")
    headlines = get_headlines(url)
    
    if headlines:
        print(f"\nFound {len(headlines)} headlines:\n")
        for i, h in enumerate(headlines[:5], 1):
            print(f"{i}. {h}")
        if len(headlines) > 5:
            print(f"... and {len(headlines)-5} more\n")
        save_to_file(headlines)
    else:
        print("No headlines found")

if __name__ == "__main__":
    main()