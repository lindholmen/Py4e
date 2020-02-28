import sqlite3
import requests
from bs4 import BeautifulSoup


def scrape(url):
    response = requests.get(url)
    mysoup = BeautifulSoup(response.text, "html.parser")
    articles = mysoup.select("article")
    bookdata = []
    for article in articles:
        title = article.select("h3 > a")[0]['title']
        # print(title)
        star_property = article.select("p")[0]["class"][1]
        if star_property == "One":
            star = 1
        elif star_property == "Two":
            star = 2
        elif star_property == "Three":
            star = 3
        elif star_property == "Four":
            star = 4
        else:
            star = 5

        price = float(article.select(".price_color")[0].get_text()[2:])

        booktuple = (title,price,star)
        bookdata.append(booktuple)

    return bookdata

def savebooks(bookdata):
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("CREATE TABLE Books(title TEXT, price REAL, star Integer);")
    c.executemany("INSERT INTO Books VALUES (?,?,?)", bookdata)
    conn.commit()
    conn.close()


data = scrape("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
savebooks(data)
