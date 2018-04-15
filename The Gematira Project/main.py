#!/usr/bin/python3
# coding=utf-8
# Gematria project

""" A project to analyse and calculate the numerical values of the torah """

from Torah_class import Torah
from data import TORAH
from miscellaneous_functions import print_all_in_list, output_list_to_file

# below goes through the list TORAH and makes a object for each and adds it to all_verses[]
all_verses = []
for book_num, book in enumerate(TORAH, start=1):
    for chapter_num, chapter in enumerate(book, start=1):
        for verse_num, verse in enumerate(chapter, start=1):
            all_verses.append(Torah(verse, book_num, chapter_num, verse_num))

# below orders the verses and puts it in a list ordered verses
ordered_verses = []
for i in range(Torah.smallest_value, Torah.largest_value + 1):
    # +1 is necessary because it will not = Torah.largest_value\
    # instead teh highest i will = will be i = Torah.largest_value - 1
    for verse in all_verses:
        if verse.value == i:
            ordered_verses.append(verse)

# below outputs both lists to a file
output_list_to_file(all_verses, "all verses file.txt")
output_list_to_file(ordered_verses, "ordered verses file.txt")

# below output both lists to the console
print_all_in_list(all_verses)
print("\n\n\n\n\nVerses ordered")
print_all_in_list(ordered_verses)

# TODO CHECK AND VALIDATE
# TODO make tests and if don't make tests REMOVE IT FROM THE README
