#! /usr/bin/env python3

import webbrowser
import sys
import pyperclip
import requests

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
    print("address:", address)

else:
    address = pyperclip.paste()
    print("address is :", address)


#webbrowser.open("https://www.google.com/maps/place/" + address)

# download a webpage using requests.get(url)

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
playfile = open("romeoandjuliet.txt","wb")
count_of_chunk = 0
for chunk in res.iter_content(100000): # 100 kb as a chunk
    count_of_chunk = count_of_chunk + 1
    numbersOfBytesWritten = playfile.write(chunk)

print("numbers of bytes written:", numbersOfBytesWritten)
print("count of chunk:",count_of_chunk)
playfile.close()
print("type of response", type(res))
print(res.status_code)
if res.status_code == requests.codes.ok:
    print("the status code means ok")
print("length:", len(res.text))
print("first 21 characters:",res.text[:21])


# try:
#     res = requests.get("https://inventwithpython.com/page_that_does_not_exist")
#     res.raise_for_status()
# except Exception as err:
#     print("there is a problem: %s" % err)


# use beautiful soup 4
import bs4
try:
    res = requests.get("http://nostartch.com")
    res.raise_for_status()
    nostartsoup = bs4.BeautifulSoup(res.text,"html.parser")
    print("type of bs4 object:",type(nostartsoup))

    exampleFile = open('example.html')
    examplesoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")
    listOfTags = examplesoup.select("#author")  # 传入selector as a string 多个中间用空格

    # <span id="author">Al Sweigart</span>
    print("tag included contents:",str(listOfTags[0]))

    print("only contents:",listOfTags[0].get_text()) # 抓取TAG中间内容 # equals getText()
    print("name of the tag:", listOfTags[0].name) # span

    print()

    print("attributes dictionary with attributes and values:", listOfTags[0].attrs) # 返回attributes和value of that attribute的字典
    print("first way to get attributes value:", listOfTags[0].get("id"))
    print("second way to get attributes value:", listOfTags[0].attrs["id"])
    print("third way to get attributes value:", listOfTags[0]["id"])
    print("Fourth way to get attributes value:", examplesoup.find("span")["id"])

    print("")

    listOfPtags = examplesoup.select('p')
    print("p elements contents are:",listOfPtags[0].getText(),listOfPtags[1].getText(),listOfPtags[2].getText())
    listofClassTags = examplesoup.select(".slogan")
    print("class of slogan:", str(listofClassTags[0 ]))

    listOfPTagDirectionUnderDiv = examplesoup.select("div > p")
    print("p elements directly under div:", str(listOfPTagDirectionUnderDiv[0]), " length:", len(listOfPTagDirectionUnderDiv))

except Exception as err:
    print("there is a problem in bs4 exercise：%s" % err)


print()
print()

# webscraping https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import DictWriter

try:
    res = requests.get("https://www.rithmschool.com/blog")
    res.raise_for_status()
    rithmschool_soup = BeautifulSoup(res.text,"html.parser")
    listOfArticles = rithmschool_soup.find_all("article")
    with open("webscraping-rithmschool.csv","w") as filehandler:
        mywriter = DictWriter(filehandler, fieldnames = ("Title", "Link", "Date"))
        mywriter.writeheader()
        for article in listOfArticles:
            a_tag = article.find("a")
            Title = a_tag.get_text()
            Link = "https://www.rithmschool.com" + a_tag["href"]
            #Date = article.find("time")["datetime"]
            Date = article.select("div > h4 > small")[0].get_text()
            print(Title,Link,Date)
            mywriter.writerow({"Title":Title,
                               "Link":Link,
                               "Date":Date})
except Exception as err:
    print("Something went wrong:", err)