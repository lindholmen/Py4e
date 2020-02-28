
import requests
import json
import os
import time
import random

import jieba
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


MASK_IMAGE = "Huan.jpeg"
#FILE_PATH = "JDcomment.txt"
FILE_PATH = "JDcomment3.txt"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
#url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4827&productId=1263013576&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1"
#url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2847&productId=7434156&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1"
url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2847&productId=100001550349&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1"

FONT_PATH = "/Library/Fonts/Songti.ttc"

def requestData(url, user_agent):
    header = {"user-agent":user_agent,"Referer": "https://item.jd.com/1263013576.html"}
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
    for i in range(100):
        new_url = url.format(i)
        print("Start to scrape with the URL", new_url)
        download_comment(new_url,header)


def download_comment(new_url,header):
    try:
        content = requests.get(new_url, headers=header)
        content.raise_for_status()
        json_str = content.text[26:-2]
        json_obj = json.loads(json_str)
        for user_comment in json_obj["comments"]:
            individual_comment = user_comment["content"]
            with open(FILE_PATH, "a+") as file:
                file.write(individual_comment + '\n')
                print(individual_comment)
        time.sleep(random.random() * 5)
    except Exception as err:
        print("failed:", err)

def word_cutting():
    with open(FILE_PATH) as file:
        cmt_txt = file.read()
        word_list = jieba.cut(cmt_txt,cut_all=True)
        return " ".join(word_list)

def wordcloud_generating():
    wc_mask = np.array(Image.open(MASK_IMAGE))
    wordcloud = WordCloud(background_color="white",
                          max_words=2000,
                          mask = wc_mask,
                          scale = 4,
                          max_font_size=50,
                          random_state=42,
                          font_path=FONT_PATH).generate(word_cutting())

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    #requestData(url,USER_AGENT)
    wordcloud_generating()

