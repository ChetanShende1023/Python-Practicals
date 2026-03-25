"""
Lab Assignment-2
Question: Create a Library Management System with the following mechanisms:
a) Design classes for Book, Member, and Library.
b) Implement methods for adding books, lending books to members, 
   returning books, and displaying book information.
c) Create a menu-driven interface for the library management system.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_lent = False  # Track if the book is currently borrowed

class Member:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        # Method to add a new book object to the library list
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def lend_book(self, title, member_name):
        # Method to lend a book if it exists and is available
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_lent:
                book.is_lent = True
                print(f"Book '{book.title}' lent to {member_name}.")
                return
        print("Error: Book not available or not found.")

    def return_book(self, title):
        # Method to mark a borrowed book as available
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_lent:
                book.is_lent = False
                print(f"Book '{book.title}' returned successfully.")
                return
        print("Error: Return failed. Check title or availability.")

    def display_books(self):
        # Method to list all books and their current status
        if not self.books:
            print("The library is currently empty.")
            return
        print("\n--- Library Inventory ---")
        for book in self.books:
            status = "Lent" if book.is_lent else "Available"
            print(f"Title: {book.title:20} | Author: {book.author:15} | Status: {status}")

def menu():
    my_library = Library()
    
    while True:
        # Menu-driven interface
        print("\n--- LIBRARY SYSTEM MENU ---")
        print("1. Add Book")
        print("2. Lend Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            t = input("Title: "); a = input("Author: ")
            my_library.add_book(t, a)
        elif choice == '2':
            t = input("Title to lend: "); m = input("Member Name: ")
            my_library.lend_book(t, m)
        elif choice == '3':
            t = input("Title to return: ")
            my_library.return_book(t)
        elif choice == '4':
            my_library.display_books()
        elif choice == '5':
            print("Exiting System...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
