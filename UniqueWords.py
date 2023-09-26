import re


def get_words(s):
    """ Extract a list of words from string s.

    Args:
        s (str): a string containing one or more words.

    Returns:
        list of str: a list of words from s converted to lower-case.
    """
    words = list()
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words


class UniqueWords:
    def __init__(self):
        self.all_words = set()
        self.unique_words = set()
        self.words_by_file = {}

    def add_file(self, filename, key):
        """Read file and extract words.
        Args:
            filename (str): The path to the file that has to be read
            key (str): A nickname for the file
        """
        with open(filename, 'r') as file:
            content = file.read()

        words = get_words(content)
        words_set = set(words)

        self.words_by_file[key] = words_set
        self.unique_words -= words_set

        newwords = words_set - self.all_words
        self.unique_words.update(newwords)
        self.all_words.update(newwords)

    def unique(self, key):
        """Return the set of words unique to the file
        Args:
            key (str): A nickname for the file previously read.
        """
        return self.words_by_file[key].intersection(self.unique_words)
