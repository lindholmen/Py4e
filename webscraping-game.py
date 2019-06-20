import requests
from bs4 import BeautifulSoup
import re
from random import choice

encyclopedia = []
website_link = "http://quotes.toscrape.com"

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

def fetch_author_info(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        author_soup = BeautifulSoup(res.text,"html.parser")
        raw_info = author_soup.select(".author-description")[0].get_text()
        return raw_info
    except Exception as err:
        print("Error occurred when fetching author info", err)

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

def initialize_to_get_user_input():
    print("\nGuess who said this:")
    random_person = choice(encyclopedia)
    print(random_person[0])
    user_input = input("Your guessed name is :")
    return user_input, random_person

def is_correct_answer(user_input, random_person):
    user_input.strip()
    author_name = random_person[1] + " " + random_person[2]
    if user_input.lower() == author_name.lower():
        return True
    else:
        return False

def print_tips(guess_times, random_person):
    if guess_times == 3:
        print(f"Tips>The person's first name starts with '{random_person[1][0]}'")
    elif guess_times == 2:
        print(f"Tips>The person's last name starts with '{random_person[2][0]}'")
    elif guess_times == 1:
        print(f"Tips>The person's bio is following:")
        print(random_person[4])
    else:
        print("Sorry you failed in guessing")

webscraping_page(website_link)
next_link = get_next_link(website_link)
while next_link:
    webscraping_page(next_link)
    next_link = get_next_link(next_link)

user_choice = "y"
while user_choice == "y":
    user_input, random_person = initialize_to_get_user_input()
    guess_times = 4
    while guess_times:
        guess_times -= 1
        if not is_correct_answer(user_input, random_person):
            print(f"Incorrect! You have {guess_times} chance(s) left!")
            print_tips(guess_times, random_person)
            if guess_times:
                user_input = input("Your guessed name is :")
            else:
                print(f"Correct answer: {random_person[1]} {random_person[2]} \n")
                user_choice = input("Wanna play again? Type 'y' to continue, else quit:")
        else:
            user_choice = input("You are so smart!! Wanna play again? Type 'y' to continue, else quit:")
            break

print("Bye bye!")
