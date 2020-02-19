import requests
import pyfiglet
import termcolor
import random

mytext = pyfiglet.figlet_format("Dad Joke 3000")
asciitext = termcolor.colored(mytext, color = "magenta", attrs=["bold"])
print(asciitext)

url = "https://icanhazdadjoke.com/search"
user_term = input("Let me tell you a joke! Give me a topic (press enter or quit to exit):  \n ")
while user_term != "quit" and user_term != "":
    try:
        res = requests.get(url, headers={"Accept": "application/json"}, params={"term": user_term})
        if res.status_code == 200:
            dict_data = res.json()  # type is dict
            #print("this is a dictionary's :", dict_data)
            joke_size = len(dict_data["results"])
            if joke_size == 1:
                print(f"I have got one joke about {user_term}. Here it is:")
                print(dict_data["results"][0]["joke"])
            elif joke_size > 1:
                print(f"i have got {joke_size} jokes about {user_term}. Here is one:")
                print(random.choice(dict_data["results"])['joke'])
            else:
                print(f"Sorry, I don't have any jokes about {user_term}. Please try again.")
            user_term = input("Let me tell you a joke! Give me a topic: \n")
    except:
        print("Connection error!")
        break

#res = requests.get(url, headers = {"Accept":"text/plain"})

# print("status code", res.status_code)
# print("headers:", res.headers)
# print("text:", res.text) # type is str

#
#
# num = 0
# for i in dict_data["results"]:
#     num += 1
#     print(f"{num}.", i["joke"])