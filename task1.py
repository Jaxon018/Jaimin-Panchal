import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get the HTML content of the webpage
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to parse the HTML content and extract data
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        books.append({'title': title, 'price': price})
    return books

# Function to save the data in CSV format
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Function to save the data in JSON format
def save_to_json(data, filename):
    df = pd.DataFrame(data)
    df.to_json(filename, orient='records', indent=4)

# Main function to run the web scraping
def main():
    url = 'http://books.toscrape.com/'
    html = get_html(url)
    if html:
        books = parse_html(html)
        save_to_csv(books, 'books.csv')
        save_to_json(books, 'books.json')
        print(f"Data saved to books.csv and books.json")
    else:
        print("Failed to retrieve the webpage")

if __name__ == "__main__":
    main()
