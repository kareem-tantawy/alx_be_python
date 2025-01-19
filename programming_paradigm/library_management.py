"""Library Management System Based on OOP concepts"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def change_book_status(self, status):
        self._is_checked_out = status

    def get_status(self):
        return self._is_checked_out


class Library:

    def __init__(self):
        self._books = []

    def add_book(self, new_book):
        self._books.append(new_book)

    def check_if_book_exists(self, book_name):
        try:
            for book in self._books:
                if book_name == book.title:
                    return True
            return False
        except Exception:
            print("Error: failed in checking if the book exists")

    def get_book(self, book_name):
        try:
            if self.check_if_book_exists(book_name):
                for book in self._books:
                    if book_name == book.title:
                        return book
            else:
                return None
        except Exception:
            print("Error: failed in getting the book")

    def check_book_status(self, book_name):
        try:
            if self.check_if_book_exists(book_name):
                return self.get_book(book_name).get_status()
            else:
                return None
        except Exception as e:
            print(f"Error in status: {e}")

    def check_out_book(self, book_name):
        try:
            if self.check_if_book_exists(book_name):
                if not self.check_book_status(book_name):
                    self.get_book(book_name).change_book_status(True)
                else:
                    print(f"Sorry, this book has been sold")
            else:
                print(f"Sorry, but this book doesn't exist")
        except ValueError as ve:
            print(f"Error: {ve}")
        except AttributeError as ae:
            print(f"Error: {ae}")

    def return_book(self, book_name):
        try:
            if self.check_book_status(book_name):
                self.get_book(book_name).change_book_status(False)
            elif self.check_if_book_exists(book_name):
                print(f"Sorry, this book still in the repository")
            else:
                print(f"Sorry, but this book doesn't exist")

        except ValueError as ve:
            print(f"Error: {ve}")
        except AttributeError as ae:
            print(f"Error: {ae}")

    def list_available_books(self):
        for book in self._books:
            if not book.get_status():
                print(f"{book.title} by {book.author}")
