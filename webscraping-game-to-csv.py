import requests
from bs4 import BeautifulSoup
import re
from csv import writer


encyclopedia = []
website_link = "http://quotes.toscrape.com"


def fetch_author_info(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        author_soup = BeautifulSoup(res.text,"html.parser")
        raw_info = author_soup.select(".author-description")[0].get_text()
        return raw_info
    except Exception as err:
        print("Error occurred when fetching author info", err)

def webscraping_page(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        quote_soup = BeautifulSoup(res.text, "html.parser")
        quote_list = quote_soup.select(".quote")
        for quote_block in quote_list:
            quote_text = quote_block.select(".text")[0].get_text()
            author = quote_block.select("span > small")[0].get_text()
            name = author.split(" ")
            if len(name) == 2:
                firstname = name[0]
                lastname = name[1]
            elif len(name) == 3:
                firstname = name[0]
                lastname = name[2]

            link_to_author = website_link + quote_block.select("a")[0]["href"]
            raw_author_info = fetch_author_info( link_to_author)

            # matching the regex to filter out the names in the biography
            regex = re.compile(r'{}|{}(\S)*'.format(firstname,lastname))
            filtered_bio = regex.sub("****", raw_author_info)

            quote_info = [quote_text, firstname, lastname, link_to_author, filtered_bio]
            encyclopedia.append(quote_info)

    except Exception as err:
        print("there is a problem in bs4 exercise:" , err)

def get_next_link(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        quote_soup = BeautifulSoup(res.text, "html.parser")
        if len(quote_soup.select(".next")) > 0:
            next_link = website_link + quote_soup.select(".next")[0].select("a")[0]["href"]
            return next_link
        return None
    except Exception as err:
        print("Error occurred when getting next link", err)

webscraping_page(website_link)
next_link = get_next_link(website_link)
while next_link:
    webscraping_page(next_link)
    next_link = get_next_link(next_link)

with open("quotes.csv","w") as filehandler:
    mywriter = writer(filehandler)
    mywriter.writerow(["quote_text", "firstname", "lastname", "link_to_author", "filtered_bio"])
    for quote in encyclopedia:
        mywriter.writerow(quote)
