

import requests

url = "http://music.163.com/weapi/cloudsearch/get/web?csrf_token="

download_url = "http://music.163.com/song/media/outer/url?id={}.mp3"

headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

data = {
"params": "SRf31nf+qVxQ/jK6CZutenhFUObNdzE+A4lbHk+M2lDymjRPZCo5Efu7OhVPNIMHjDOTt7x4ojD9G4sJYvAkNEhO6l8MRoTyQhRXg2LQ8x2Baf/d8gWXco7hoBYMS8FCh+67ubn+hlbEO8yjsKlZZgyal/oBRRCAUR3cL1R53SlrSdniMVg7GJy0/ZvofNmNAPDpep+uapCjVaxI5ZPyIXB9hNBwSE7Y+BVK2SmTt/hXmkSt4BLiV6eAevItc1hdjR9hNr3EUfnaXGN7C/8gCw==",
"encSecKey": "bcf051319ba5f94bdce3913172cfe84c78d72ea0f4676030879389827dcc427bdf6652ee416cb1f377ba914f01820cfed48fc4314460ce90f7e519d7db38709ba84e501e9ce4528e7c1f3c176c7480f96729a23fa0901fa06e36c2027ec0a4af75bb3c53a0ebb0c9951c4ef93462e20735304916714ef5896c4af3f3004d000c"
}

response =requests.post(url,headers=headers, data=data).json()

id_list = response['result']['songs']

for item in id_list:
    song_id = item['id']
    song_name = item['name']
    newurl = download_url.format(song_id)
    response_data = requests.get(newurl, headers= headers).content #stream data

    with open('downloadsongs/'+ song_name + '.mp3', 'wb') as file_handler:
        file_handler.write(response_data)
        print(song_name + " has been downloaded")