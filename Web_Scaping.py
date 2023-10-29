import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []

    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = ', '.join(tag.text for tag in quote.find_all('a', class_='tag'))
        quotes.append([text, author, tags])

  
    with open('quotes.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Quote', 'Author', 'Tags'])
        csv_writer.writerows(quotes)

    print(f"Scraped {len(quotes)} quotes and saved to quotes.csv.")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
