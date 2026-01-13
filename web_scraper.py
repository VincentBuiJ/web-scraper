import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

#Find all quote containers (each contains quote, author, and tags together)
quote_divs = soup.find_all('div', class_='quote')

#Open CSV for writing
with open('quotes.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Author', 'Quote', 'Tags'])

    for div in quote_divs:
        #Extract quote from this div
        quote = div.find('span', class_='text').text.strip('""')

        #Extract author from this div
        author = div.find('small', class_='author').text

        #Extract multiple tags from this div
        tag_elements = div.find_all('a', class_='tag')
        tags = ','.join([tag.text for tag in tag_elements])

        #Write to CSV file
        writer.writerow([author, quote, tags])

print("✅ Quotes saved to quotes.csv!")

