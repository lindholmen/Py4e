#!/usr/bin/env python
import requests
from urllib import request
from urllib.parse import quote
import threading
import re
import os
from http import client
import string



"""webscraping_QQlive.py: A simple webscraping task on Duitang.com"""


USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"

# 基于用户习惯：ip代理池，random, time. 验证码的反爬虫（Python爬虫利器之Selenium 添加代理服务器）动态页面的反爬虫 ajax.模拟数据 登录反爬虫，找cookie

# 长连接池返回相关cookie,不断开链接. 长连接适用于要进行大量数据传输的情况，如：数据库，redis,memcached等要求快速，数据量大的情况下。
# 长连接通过心跳机制（通信数据很少）来进行连接状态的监测，断后重新进行连接
# 短连接池:HTTP连接是短连接，每发起一次请求都建立TCP连接,响应请求后就断开连接，这样防止客户端长期占用服务器的资源，维持连接是要占用线程的。
client.HTTPConnection._http_vsn = 10
client.HTTPConnection._http_vsn_str = "HTTP/1.0"

pattern_01 = r'<div id="content">.*?<h2>(.*?)</h2>'
pattern_02 = r'<p style=".*?"><img.*?src="(.*?)".*?/>.*?</p>'
pattern_03 = r'^.*/(.*?)$'

class GetManPic(object):
    def __init__(self,http_str):
        self.user_agent = USER_AGENT
        self.url = http_str

    # Step 1. request data
    def requestData(self,url,user_agent):
        req = request.Request(url)
        req.add_header("User-Agent",user_agent)
        # status code 200
        res = request.urlopen(req,timeout=8)
        # get string content
        content = res.read().decode("utf-8")
        return content

    def getPageData(self):
        content = self.requestData(self.url,self.user_agent)
        regex = re.compile(pattern_01,re.S)
        name_result = re.search(regex,content)
        name_str = name_result.group(1)
        dir_path = self.makedir(name_str)

        pic_regex = re.compile(pattern_02,re.S)
        suffix_regex = re.compile(pattern_03,re.S)

        while True:
            print(f"fetching data from {name_str}")
            pic_items = re.findall(pic_regex,content)
            print("pic_items:",pic_items)
            for item in pic_items:
                pics = re.search(suffix_regex,item) # or suffix_regex.search(item)
                pic_name = pics.group(1)
                file_dir = os.path.join(dir_path,pic_name)

                url = quote(item, safe = string.printable)
                print("url:",url)
                req = request.Request(url)
                req.add_header("User-Agent", USER_AGENT)
                response = request.urlopen(req)
                pic_data = response.read()

                with open(file_dir,"wb") as file:
                    file.write(pic_data)

            print("Successful!")
            break;



    def makedir(self,dir_name):
        new_path = os.path.join(os.getcwd(),dir_name)
        if os.path.exists(new_path):
            print("current directory already exists\n")
            return
        else:
            os.makedirs(new_path)
            print("directory created successfully!\n")
            return new_path





if __name__ == "__main__":
    get = GetManPic("http://enrz.com/fhm/2016/12/17/74914.html")
    get.getPageData()






