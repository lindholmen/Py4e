from random import choice
from csv import reader

encyclopedia = []

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

with open("quotes.csv") as filehandler:
    csv_rows = reader(filehandler)
    table_header = next(csv_rows)  # skip the table header or using list(csv_rows) to cast it to a list of lists!

    for row in csv_rows:
        quote_text, firstname, lastname, link_to_author, filtered_bio = row[0], row[1], row[2],row[3],row[4]
        encyclopedia.append([quote_text, firstname, lastname, link_to_author, filtered_bio])


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