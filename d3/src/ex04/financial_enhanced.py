#!/usr/bin/env python3
import httpx, sys
from bs4 import BeautifulSoup

def financial(ticker, field):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com/',
        'DNT': '1'
    } 
    cookies = {
        'B': '1dqj8u3mhq4re&b=3&s=0b',
        'A1': 'd=AQABBK0zq2MCEGQ6y1pQ3uYk6i0HuQZz9l8FEgEBAQHSoWNYZAAAAAA_eJwNwTQJAAAA&S=AQAAAk3tq9l3Z9WJZvq3K1Yw7vU',
        'A3': 'd=AQABBK0zq2MCEGQ6y1pQ3uYk6i0HuQZz9l8FEgEBAQHSoWNYZAAAAAA_eJwNwTQJAAAA&S=AQAAAk3tq9l3Z9WJZvq3K1Yw7vU'
    }
    
    with httpx.Client(follow_redirects=True) as client:
        r = client.get(url, headers=headers, cookies=cookies, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('div', class_='tableBody yf-9ft13')
        if not table:
            raise Exception("")
        
        rows = table.find_all('div', class_='row lv-0 yf-t22klz')
        for row in rows:
            title_col = row.find('div', class_='column sticky yf-t22klz').find('div', class_='rowTitle yf-t22klz')
            if title_col and title_col.get('title') == field:
                values = [col.get_text().strip() for col in row if col.get_text().strip()]
                return tuple(values)
        raise ValueError(f"Field '{field}' not found")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Wrong cli params num: {len(sys.argv)}, expected 3")
        sys.exit(1)
    try:
        print(financial(sys.argv[1], sys.argv[2]))
    except Exception as e:
        print(f"Exception {str(e)}")
