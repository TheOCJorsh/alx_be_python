class Book:
    def __init__(self, title, author):
        self.title = title               # Public attribute
        self.author = author             # Public attribute
        self._is_checked_out = False     # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check whether the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Attempt to check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"You checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in library.")

    def return_book(self, title):
        """Attempt to return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"You returned '{title}'.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book '{title}' not found in library.")

    def list_available_books(self):
        """Print all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]

        if not available_books:
            print("No books are currently available.")
            return

        for book in available_books:
            print(f"- {book.title} by {book.author}")
