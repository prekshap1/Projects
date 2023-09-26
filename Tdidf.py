""" Use tf-idf to identify the most important words in a document
relative to other documents in a corpus. """

from argparse import ArgumentParser
from collections import Counter
from math import log
from pathlib import Path
import re
import sys


class TfidfCalculator:
    def __init__(self):
        self.tf = {}
        self.df = Counter()

    def read_file(self, filename):
        """ Read a file and update the tf and df attributes.

        Args:
            filename (str): Path to the file to be read.

        Returns:
            None
        """
        with open(filename, 'r') as file:
            content = file.read()
            words = get_words(content)

            # Update tf dictionary
            self.tf[filename] = Counter(words)

            # Update df Counter
            unique_words = set(words)
            self.df.update(unique_words)

    def important_words(self, filename, num_words=10):
        """ Calculate the important words in a file based on tf-idf metric.

        Args:
            filename (str): Path to the file for which important words are calculated.
            num_words (int, optional): Number of important words to return. Defaults to 10.

        Returns:
            dict: Dictionary containing the top num_words words as keys and their corresponding tf-idf scores as values.
        """
        total_words = sum(self.tf[filename].values())
        total_documents = len(self.tf)

        tfidf_scores = {
            word: (self.tf[filename][word] / total_words) * log(total_documents / self.df[word])
            for word in self.tf[filename]
        }

        sorted_words = sorted(tfidf_scores, key=tfidf_scores.get, reverse=True)

        if num_words is None:
            num_words = len(sorted_words)

        important = {
            word: tfidf_scores[word]
            for word in sorted_words[:num_words]
        }

        return important


def get_words(s):
    """ Extract a list of words from string s.

    Args:
        s (str): A string containing one or more words.

    Returns:
        list: A list of words from s converted to lower-case.
    """
    words = []
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words


def main(directory, files, pattern="*", num_words=10):
    """ Read files from a directory, and identify the most important words in one or more specified files.

    Args:
        directory (str or Path): Path to a directory containing a corpus of texts to read in.
        files (list of (str or Path)): Paths to files for which the user wants to identify the most important words.
        pattern (str): Glob pattern for files to include from directory. (Default: "*")
        num_words (int): The number of important words to report for each specified file. (Default: 10)

    Returns:
        None
    """
    calc = TfidfCalculator()
    for document in Path(directory).glob(pattern):
        calc.read_file(str(document))

    if not files:
        files = sorted(calc.tf)

    for n, filename in enumerate(files):
        if n != 0:
            print()
        print(f"Most important words in {str(filename)}:")
        important = calc.important_words(str(filename), num_words=num_words)
        for word, score in important.items():
            print(f"  {word}: {score}")


def parse_args(arglist):
    """ Parse command-line arguments.

    Args:
        arglist (list of str): Command-line arguments to parse.

    Returns:
        namespace: A namespace with the following variables:
            directory (pathlib.Path)
            files (list of pathlib.Path)
            pattern (str)
            num_words (int)
    """
    parser = ArgumentParser()
    parser.add_argument("directory", type=Path, help="Directory containing documents to read in")
    parser.add_argument("files", type=Path, nargs="*", help="File(s) to identify important words in")
    parser.add_argument("-p", "--pattern", default="*", help="Glob pattern specifying which files to read in")
    parser.add_argument("-n", "--num_words", type=int, default=10, help="Number of words to display (default is 10)")
    args = parser.parse_args(arglist)

    for path in args.files:
        if not path.exists():
            sys.exit(f"File {str(path)} not found")

    pattern = args.directory / args.pattern
    if not path.match(str(pattern)):
        sys.exit(f"file {str(path)} is not in the specified corpus"
            f" ({str(pattern)})")
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.directory, args.files, pattern=args.pattern, num_words=args.num_words)
