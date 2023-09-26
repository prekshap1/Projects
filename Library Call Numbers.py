import re

class Book:
    """A class to represent a book with call number, title, and author."""

    def __init__(self, callnum, title, author):
        """
        Initialize the Book class.

        Args:
            callnum (str): The call number for the book.
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.callnum = callnum
        self.title = title
        self.author = author

    def __lt__(self, other):
        """
        Compare two instances of Book based on their call numbers.

        Args:
            other (Book): Another instance of the Book class.

        Returns:
            bool: True if self.callnum sorts before other.callnum, False otherwise.
        """
        return self.sort_key() < other.sort_key()

    def __repr__(self):
        """
        Return a string representation of the Book object.

        Returns:
            str: A string representation of the Book object.
        """
        return f"Book('{self.callnum}', '{self.title}', '{self.author}')"

    def sort_key(self):
        """
        Return a tuple representing the sort key for the book's call number.

        Returns:
            tuple: A tuple representing the sort key for the book's call number.
        """
        match = re.match(r"([A-Z]+)?(\d+(\.\d+)?)([A-Z])?(\d+)?", self.callnum)
        if match:
            group1, number, _, group2, number2 = match.groups()
            number = float(number) if '.' in number else int(number)
            group1 = group1 or ''
            group2 = group2 or ''
            number2 = int(number2) if number2 else 0
            return (group1, number, group2, number2)
        return ()

def read_books(filename):
    """
    Read book information from a file and return a list of Book objects.

    Args:
        filename (str): The path to the file containing book information.

    Returns:
        list: A list of Book objects.
    """
    books = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            title, author, callnum = line.strip().split('\t')
            book = Book(callnum, title, author)
            books.append(book)
    return books

def print_books(books):
    """ Print information about each book, in order. """
    for book in sorted(books):
        print(book)

def main(filename):
    """ Read book information from a file, sort the books by call number,
    and print information about each book. """
    books = read_books(filename)
    print_books(books)

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing book information")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)
