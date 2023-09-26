from argparse import ArgumentParser
import re
import sys

class Book:
    """Represents a book with call number, title, and author."""

    def __init__(self, callnum, title, author):
        """Initialize the Book object with call number, title, and author."""
        self.callnum = callnum
        self.title = title
        self.author = author

    def __lt__(self, other):
        """Compare two Book objects based on their call numbers."""
        return self.compare_callnum(self.callnum, other.callnum)

    def __repr__(self):
        """Return a string representation of the Book object."""
        return f"Book('{self.callnum}', '{self.title}', '{self.author}')"

    def compare_callnum(self, callnum1, callnum2):
        """Compare two call numbers based on Library of Congress sorting rules."""
        # Extract the individual parts from the call numbers
        parts1 = self.parse_callnum(callnum1)
        parts2 = self.parse_callnum(callnum2)

        # Compare each part of the call numbers according to the sorting rules
        for i in range(len(parts1)):
            if parts1[i] < parts2[i]:
                return True
            elif parts1[i] > parts2[i]:
                return False

        # If all parts are equal, compare the entire call number as strings
        return callnum1 < callnum2

    def parse_callnum(self, callnum):
        """Parse the call number into its various parts."""
        # Split the call number into the class, number, cutter, and year components
        class_num, cutter, year = re.findall(r"([A-Z]+|\d+\.?\d*|[A-Z]\d+|\d+)$", callnum)

        # Split the class into separate letters (if present)
        class_letters = re.findall(r"[A-Z]", class_num)
        class_number = re.findall(r"\d+", class_num)

        return class_letters + class_number + [cutter, year]

def read_books(filename):
    """Read book information from a file and return a list of Book objects."""
    books = []
    with open(filename, 'r') as file:
        for line in file:
            title, author, callnum = line.strip().split('\t')
            book = Book(callnum, title, author)
            books.append(book)
    return books

def print_books(books):
    """Print information about each book, in order."""
    for book in sorted(books):
        print(book)

def parse_args(arglist):
    """Parse command-line arguments and return the parsed values as a namespace."""
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing book information")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    books = read_books(args.filename)
    print_books(books)
