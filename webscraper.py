from bs4 import BeautifulSoup
import requests
import sys
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_all_items(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find("ul", {"class": "b-list__items_nofooter"}).findAll("li", {"class": "s-item"})
    return items

def get_item_data(item):
    try:
        title = item.find({"h3": "s-item__title"}).text
    except:
        title = ''
    try:
        link = item.find({"a":"href"}).text
        print(link)
    except:
        link = ''    
    try:
        price = item.find("span", {"class": "s-item__price"}).text
    except:
        price = ''
    data = {'title': title,
            'price': price,
            'link': link}
    return data

def write_csv(i, data):
    with open('notebooks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
        data['price'],data['link']))
        print(i, data['title'], 'parsed')

def main():
    url = 'https://www.ebay.ca/b/BMW/6006?Drive%2520Type=RWD&Make=BMW&Transmission=Manual&rt=nc'
   #for page in range(1, 5):  # count of pages to parse
    all_items = get_all_items(get_html(url + '?_pgn=1'))
    for i, item in enumerate(all_items):
        data = get_item_data(item)
        print(data)
        write_csv(i, data)


if __name__ == '__main__':
   main()