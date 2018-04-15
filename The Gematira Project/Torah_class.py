from data import BOOK_NAME_DICT
from miscellaneous_functions import calculate_gematria

"""A .py file for each verse"""


class Torah:
    """A class for each verse"""

    largest_value = 0
    smallest_value = 0

    def __init__(self, text, book_number, chapter_number, verse_number):
        self.text = text
        self.book_num = book_number
        self.book = BOOK_NAME_DICT[book_number]
        self.chapter = chapter_number
        self.verse_no = verse_number
        self.value = calculate_gematria(self.text)
        if self.value > Torah.largest_value:
            Torah.largest_value = self.value
        if self.value < Torah.smallest_value:
            Torah.smallest_value = self.smallest_value

    def __str__(self):  # TODO make output better by ensuring all is of the same length
        return "Book:" + self.book \
               + " Chapter:" + str(self.chapter) \
               + " Verse:" + str(self.verse_no) \
               + " Gematria:" + str(self.value) \
               + " text: " + self.text

    def __repr__(self):
        return self.book + ", " \
               + str(self.chapter) + ", " \
               + str(self.verse_no) + ", " \
               + str(self.value) + ", " \
               + self.text
