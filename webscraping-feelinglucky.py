#! python3
# opens several google page at once

import urllib.request
import requests, sys, webbrowser
from bs4 import BeautifulSoup
import ssl

print("googling...")


if len(sys.argv) > 1:
    kw = "+".join(sys.argv[1:])
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    link = "https://www.google.com/search?q=" + kw
    print("link:", link)
    headers = {'User-Agent': user_agent}
    try:
        #res = requests.get(link) # 得到的页面和浏览器不一致！
        request = urllib.request.Request(url=link, headers=headers)
        gcontext = ssl.SSLContext() # bypass “SSL: CERTIFICATE_VERIFY_FAILED” Error
        html = urllib.request.urlopen(request,context=gcontext).read()

        google_soup = BeautifulSoup(html,"html.parser")
        g_blocks = google_soup.select("cite.iUh30")

        for block in g_blocks:

            target_link = block.get_text()
            #webbrowser.open(target_link)
            print(target_link)

    except Exception as err:
        print("something wrong:", err)
else:
    print("Please type keywords for search as arguments: python3 xx.py keyword")

