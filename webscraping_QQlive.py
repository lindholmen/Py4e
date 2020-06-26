#!/usr/bin/env python
import requests
import urllib
import threading
import re

"""webscraping_QQlive.py: A simple webscraping task on Duitang.com"""



#test
url = "https://www.duitang.com/napi/blog/list/by_search/?kw=%E9%87%8D%E5%BA%86&start=0&limit=1000"


threads_lock = threading.BoundedSemaphore(value=10)


def get_page(url):
    # byte to string
    page = requests.get(url).content.decode("utf-8")
    return page

def findall_in_page(page_str,prefix,suffix):
    end = 0
    all_downloadurl_strings = []
    while page_str.find(prefix, end) != -1:
        start = page_str.find(prefix,end) + len(prefix)
        end = page_str.find(suffix,start)
        mystr = page_str[start:end]
        all_downloadurl_strings.append(mystr)
    return all_downloadurl_strings

def pic_urls_from_tang(pages):
    pic_urls = []
    for page in pages:
        # method 1: string.find()
        #urls = findall_in_page(page,'"path":"','"')
        #pic_urls.extend(urls)  # extend vs. append
        # method 2: regex using non-greedy match
        url_regex = re.compile(r'"path":"(.+?)"}')
        mo_for_all = url_regex.findall(page)
        pic_urls.extend(mo_for_all)
    return pic_urls

def generate_pages(searched_keyword):
    url = "https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=1000"
    pages = []
    kw = urllib.parse.quote(searched_keyword) # convert to ASCII
    for start_index in range(0,3600,100):
        url_per_page = url.format(kw, start_index)
        payload_per_hundred = get_page(url_per_page)
        pages.append(payload_per_hundred) # or consider using yield payload_per_hundred?
    return pages
def download_pic(url,name):
    try:
        res = requests.get(url)
        res.raise_for_status()
        path = "downloadpics/" + str(name) + ".jpg"
        with open(path, "wb+") as file:
            file.write(res.content)
        # release the lock
        threads_lock.release()
    except Exception as err:
        print("something wrong:", err)

def main(keyword):
    pic_urls = pic_urls_from_tang(generate_pages(keyword))
    numbers = 0
    for url in pic_urls:
        numbers += 1
        print(f"Downloading the picture of index No.{numbers}")

        # Lock it
        threads_lock.acquire()
        # Push one-pic download task to the threadpool
        t = threading.Thread(target=download_pic, args=(url, numbers))
        t.start()

main("崇明")