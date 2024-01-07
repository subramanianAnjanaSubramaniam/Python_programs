class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {'Yes' if self.is_available else 'No'}\n")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []

    def display_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Books Borrowed: {', '.join([book.title for book in self.books_borrowed])}\n")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                book.display_info()

    def display_members(self):
        print("Library Members:")
        for member in self.members:
            member.display_info()

    def borrowed_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if member and book and book.is_available:
            member.books_borrowed.append(book)
            book.is_available = False
            print(f"{member.name} borrowed '{book.title}'.")
        else:
            print("Unable to borrow the book. Please check member and book IDs.")

    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if member and book and not book.is_available and book in member.books_borrowed:
            member.books_borrowed.remove(book)
            book.is_available = True
            print(f"{member.name} returned '{book.title}'.")
        else:
            print("Unable to return the book. Please check member and book IDs.")


library = Library()

# Adding books to the library
book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)

# Adding members to the library
member1 = Member(101, "Alice")
member2 = Member(102, "Bob")
library.add_member(member1)
library.add_member(member2)

# Display available books and library members
library.display_books()
library.display_members()

# Simulating borrowing and returning books
library.borrowed_book(101, 1)
library.borrowed_book(102, 2)

library.display_books()
library.display_members()

library.return_book(101, 1) 

library.display_books()
library.display_members()