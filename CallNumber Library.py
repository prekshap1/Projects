from argparse import ArgumentParser
import re
import sys

class Book:
    """
    

    Attributes:
        callnum (str): The call number of the book in the Library of Congress system.
        title (str): The title of the book.
        author (str): The author of the book (can be an empty string if unknown).
    """
    def __init__(self, callnum, title, author):
        self.callnum = callnum
        self.title = title
        self.author = author

    def __lt__(self, other):
        """
        Compare two Book objects based on their call numbers.

        Parameters:
            self (Book): The current instance of the Book class.
            other (Book): Another instance of the Book class

        Returns:
            bool: True if self.callnum sorts before other.callnum, False otherwise.
        """
        return self._parse_callnum() < other._parse_callnum()

    def __repr__(self):
        """
        Return a formal string representation of the Book object that can be used to re-create it.

        Parameters:
            self (Book): The current instance of the Book class.

        Returns:
            str: A string that can be used to re-create the current Book instance.
        """
        return f"Book('{self.callnum}', '{self.title}', '{self.author}')"

    def _parse_callnum(self):
        """
        Helper method to parse the call number into its various parts for sorting.
        It returns a tuple that can be used for comparison in the __lt__() method.

        Parameters:
            self (Book): The current instance of the Book class.

        Returns:
            tuple: A tuple representing the parsed call number for sorting.
        """
        # Regular expression to extract various parts of the call number
        match = re.match(r'^([A-Z]+)?(\d+)?(\.\d+)?\s*([A-Z])?(\d+)?(\.\d+)?\s*(\d{4})$', self.callnum)

        if match:
            class_letters, class_number, _, cutter_letter1, cutter_number1, _, cutter_letter2, cutter_number2, year = match.groups()

            class_number = int(class_number) if class_number else 0
            cutter_number1 = float(cutter_number1) if cutter_number1 else 0
            cutter_number2 = float(cutter_number2) if cutter_number2 else 0

            return (class_letters, class_number, cutter_letter1, cutter_number1, cutter_letter2, cutter_number2, year)
        else:
            # If call number doesn't match expected pattern, return a tuple with highest priority
            return ('', 0, '', 0, '', 0, '0000')

def read_books(file_path):
    """
    Read books from a file and create a list of Book instances.

    Parameters:
        file_path (str): The path to the file containing book information.

    Returns:
        list: A list of Book instances, one per line in the file.
    """
    books_list = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            title, author, callnum = line.strip().split('\t')
            book = Book(callnum, title, author)
            books_list.append(book)

    return books_list

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
