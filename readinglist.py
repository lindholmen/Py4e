
menu_prompt = """ 
please enter one of the following options
- "a" to add a book
- "l" to list the books
- "q" to quit
- "s" to search a book
- "d" to delete a book

what would you like to do ? \n"""

selected_option = input(menu_prompt).strip().lower()

def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year: ").strip()

    with open("readinglist_books.csv","a") as file_reader:
        file_reader.write(f"{title},{author},{year}\n")


    print("Added successfully!")

def list_books(books):
    print()
    i = 1
    for book in books:
        title, author, year = book.values()
        print(f"{i}. {title}, by {author} ({year})")
        i = i+1
    print()

def get_all_books():
    books = []
    with open("readinglist_books.csv", "r") as file_reader:
        for book in file_reader.readlines():
            title, author, year = book.strip().split(",")
            books.append({
                "title":title,
                "author":author,
                "year":year
            })

    return books

def find_books():
    matching_books = []
    reading_list = get_all_books()
    search_item = input("please enter a book title to search for?\n").strip().lower()
    for book in reading_list:
          if search_item in book["title"].lower():
              matching_books.append(book)

    return matching_books


def delete_book():
    reading_list = get_all_books()
    matching_books = find_books()
    if matching_books:
        list_books(matching_books)
        total_books = len(matching_books)
        user_confirmation = input("which book do you want to delete? type 1,2,3... or 'n' if you do not want \n").strip().lower()
        while user_confirmation!="n":
            if user_confirmation.isnumeric() and int(user_confirmation)>0 and int(user_confirmation)<= total_books:
                reading_list.remove(matching_books[int(user_confirmation)-1])
                print("deleted!")
                with open("readinglist_books.csv","w") as file_reader:
                    for book in reading_list:
                        file_reader.write(f"{book['title']},{book['author']},{book['year']}\n")
                break
            else:
                print("wrong input! \n")
                user_confirmation = input("which book do you want to delete? type 1,2,3... or 'n' if you do not want \n").strip().lower()
        print("delete mission finished")
    else:
        print("Sorry we did not find any books matching that title")

while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        reading_list = get_all_books()
        if reading_list:
            list_books(reading_list)
        else:
            print("your reading list is empty")
    elif selected_option == "s":
        searched_results = find_books()
        if searched_results:
            list_books(searched_results)

    elif selected_option == "d":
        delete_book()
    else:
        print(f" The '{selected_option}' is not a valid option")

    selected_option = input(menu_prompt).strip().lower()
