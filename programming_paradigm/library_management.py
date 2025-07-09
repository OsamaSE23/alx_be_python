class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.__is_checked_out = is_checked_out

    def is_checked_out(self):
        return self.__is_checked_out

    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False


class Library:
    def __init__(self):
        self.__books = []
        self.__checked_out = []

    def add_book(self, book):
        if book.is_checked_out():
            self.__checked_out.append(book)
        else:
            self.__books.append(book)

    def list_available_books(self):
        for book in self.__books:
            print(f"{book.title} by {book.author}")

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.check_out()
                self.__books.remove(book)
                self.__checked_out.append(book)
                return

    def return_book(self, title):
        for book in self.__checked_out:
            if book.title == title:
                book.return_book()
                self.__checked_out.remove(book)
                self.__books.append(book)
                return

