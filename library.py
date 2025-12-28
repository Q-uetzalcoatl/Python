# Define the Book class
class Book:
    def __init__(self, title, author, year):
        # Initialize the book with title, author, and year
        self._title = title  # Protected attribute for the book's title
        self._author = author  # Protected attribute for the book's author
        self._year = year  # Protected attribute for the publication year

    def get_info(self):
        # Return a formatted string with book's information
        return f"{self._title} by {self._author}, {self._year}"


# Define the Library class
class Library:
    def __init__(self):
        # Initialize the library with an empty list of books
        self._books = []  # Protected attribute for storing the collection of books

    def add_book(self, book):
        # Add a book to the library's collection
        self._books.append(book)

    def remove_book(self, title):
        # Remove a book from the library by its title
        self._books = [book for book in self._books if book._title != title]

    def find_book(self, title):
        # Find a book by its title and return its information
        for book in self._books:
            if book._title == title:
                return book.get_info()  # Return book info if found
        return "Book not found."  # Return this message if the book is not in the collection

    def list_books(self):
        # Return a list of information about all books in the library
        return [book.get_info() for book in self._books]


# Optional: Define the DigitalBook class
class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        # Initialize the digital book with title, author, year, and file size
        super().__init__(title, author, year)  # Call the parent class (Book) constructor
        self._file_size = file_size  # Protected attribute for the file size

    def get_info(self):
        # Return a formatted string with book's information including file size
        return f"{self._title} by {self._author}, {self._year}, File Size: {self._file_size}MB"


# Example usage
if __name__ == "__main__":
    # Create instances of Book and DigitalBook
    book1 = Book("1984", "George Orwell", 1949)  # Create a Book instance
    book2 = DigitalBook("Python Programming", "John Doe", 2020, 2.5)  # Create a DigitalBook instance

    # Create a Library instance and add books to it
    my_library = Library()  # Create a Library instance
    my_library.add_book(book1)  # Add the first book
    my_library.add_book(book2)  # Add the second book (digital book)

    # Find and list books
    print(my_library.find_book("1984"))  # Find the book titled "1984" and print its information
    print(my_library.list_books())  # Print the information of all books in the library

    # Remove a book and list books again
    my_library.remove_book("1984")  # Remove the book titled "1984" from the library
    print(my_library.list_books())  # Print the updated list of books in the library
