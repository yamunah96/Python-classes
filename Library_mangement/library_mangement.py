# book_data dict
books_data = {
    "three mistakes of my life": {
        "author": "Chetan Bhagat",
        "description": "The 3 Mistakes of My Life follows three friends in Ahmedabad navigating business ambitions, cricket passions, religious politics, and personal missteps in early-2000s India.",
        "status": "available",
        "genre": "Contemporary Fiction"
    },
    "wings of fire": {
        "author": "Dr. A.P.J. Abdul Kalam",
        "description": "An inspirational account of Dr. Kalam's humble beginnings, his journey to becoming a pioneer in India's space and missile programmes, and his vision for the nation.",
        "status": "unavailable",
        "genre": "Autobiography"
    },
    "fourth wing": {
        "author": "Rebecca Yarros",
        "description": "Enter the brutal world of a military college for dragon riders, where Violet Sorrengail must survive deadly trials, political intrigue, and intense romance.",
        "status": "available",
        "genre": "Fantasy Romance"
    },
    "three men in a boat": {
        "author": "Jerome K. Jerome",
        "description": "A humorous account of three friends and their dog, Montmorency, as they embark on a chaotic and misadventure-filled boating holiday along the River Thames.",
        "status": "available",
        "genre": "Humorous Fiction"
    },
    "fire and blood": {
        "author": "George R.R. Martin",
        "description": "A comprehensive history of the Targaryen dynasty, chronicling the rise and fall of dragon kings, bloody civil wars, and the conquest of Westeros.",
        "status": "available",
        "genre": "Epic Fantasy"
    },
    "the mistake": {
        "author": "Elle Kennedy",
        "description": "A college romance following a hockey player who tries to win back the girl he accidentally pushed away after making a major personal misstep.",
        "status": "available",
        "genre": "Contemporary Romance"
    }
}
# borrower_data dict
borrowed_data={}

print(" ")
print("**************** Welcome To Karnataka Government Public Library*******************")

# while loop to keep the program running until the user chooses to exit
while True:
    print(" ")
    print("**************Check the Menu for more info*******************")
    print("1. Add Book\n2. Borrow Book\n3. Return Book\n4. Search Book\n5. Display Books\n6. Borrowed Book\n7. Exit")
    print(" ")

    # validation i can do in next class of using try and except block to handle the invalid input from user
    
    choice= int(input("Enter Your Choice: "))
    # check the user choice and perform the corresponding action
    if choice == 1:
        print("If You would like to add book, Kindly Provide the below information about the Book")
        print(" ")
        book_name=input("Enter the name of the book: ").lower().strip()
        

        # check this book exist in our book_data 
        if book_name in books_data:
            answer= input(f"{book_name} is already exists in libray,Would you like modifiy any details click Yes or No: ").lower().strip()
            if answer == "yes" or answer =="y":
                author=input("Enter the Author name: ").lower().strip()
                desciption= input("Enter the 1 line description about the book: ").lower().strip()
                genre= input("Enter the gener: ").lower().strip()
                books_data[book_name]['author']=author
                books_data[book_name]['description']=desciption
                books_data[book_name]["genre"]=genre

                print(f"{book_name} updated to succefully data....")
            else:
                continue
        # check this book not exist in our book_data, then add the book to the library
        if book_name not in books_data:
            author=input("Enter the Author name: ").lower().strip()
            desciption= input("Enter the 1 line description about the book: ").lower().strip()
            genre= input("Enter the gener: ").lower().strip()
            books_data[book_name]={
                "author":author,
                "description":desciption,
                "genre":genre,
                "status":"available"
            }

    elif choice==2:
        print("Kindly Enter below details to borrow a book")
        book_name= input("Enter the name of the book: ").lower().strip()
        print(" ")
        if book_name in books_data:
            # check the book status is available or not, if available then issue the book to user and update the status to unavailable
            if books_data[book_name]["status"] == "available":
                name= input("Enter your name: ").lower().strip()
                print(f"{book_name} is issued to {name} sussefully, Return the book by a week")
                books_data[book_name]["status"]= "unavailable"
                borrowed_data[book_name]={
                    "borrower_name":name,
                }
                print(borrowed_data)
            else:
                print(f"Sorry the book is not available at this moment")
        else:
            print(f"Sorry the book is not in our library")
            
    elif choice == 3:
        print("Kindly Enter below details to return a book")
        book_name= input("Enter the name of the book: ").lower().strip()
        name= input("Enter your name: ").lower().strip()
        print(" ")
        if book_name in books_data:
            # check the book status is unavailable or not, if unavailable then return the book to library and update the status to available
            if books_data[book_name]["status"] == "unavailable" and borrowed_data[book_name]["borrower_name"]==name:
                borrowed_data.pop(book_name)
                print(f"{name} is returned {book_name} sussefully\nThanks For visting !!")
                books_data[book_name]["status"]= "available"
            else:
                print(f"Sorry the book is not issued to you, kindly return correct book ")
        else:
            print(f"Kindly return correct book name")

    elif choice == 4:
        # search the book in library and display the details of the book if available
        print("Kindly Enter below details to search a book")
        book_name= input("Enter the name of the book: ").lower().strip()
        if book_name in books_data:
            print("====================Book Details=====================================")
            print(f"Book Name: {book_name}\nAuthor: {books_data[book_name]["author"]}\nAbout: {books_data[book_name]['description']}\nStatus: {books_data[book_name]["status"]}")

        else:
            print(f"{book_name} is not available in library,These are the similar book available")
            for name,data in books_data.items():
                if book_name in name:
                    print(name)
            

    elif choice ==5:
        print("=============================== Books ==================================")
        # display the total number of books, available books and unavailable books in the library
        total_books= len(books_data)
        available_books=0
        unvailable_books=0
        for book,data in books_data.items():
            if data["status"] =="available":
                available_books+=1
            if data["status"] =="unavailable":
                unvailable_books+=1


        print(f"Total Books: {total_books}\nAvailable :{available_books}\nUnAvailable :{unvailable_books}")
        print(" ")

        # display the details of all the books in the library
        for book_name,data in books_data.items():
            print(" ")
            print(f"Book Name: {book_name}")
            print(f"Author :{data["author"]}")
            print(f"About: {data['description']}")
            print(f"Status: ",data["status"])
    #I have added additional menu to check borrowed books
    elif choice ==6:
        print("Borrowed Books:")
        # display the details of all the borrowed books in the library
        if borrowed_data=={}:
            print("No books are borrowed yet.")
        else:
            for book_name, borrower_info in borrowed_data.items():
                print(f"Book: {book_name}, Borrower: {borrower_info['borrower_name']}")
    elif choice ==7:
        # Exit the program
        print("Thanks Visiting the Library,Enjoy your reading")
        break
    else:
        print("Select the valid choice.Try again!!..........")
