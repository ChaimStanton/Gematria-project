from data import VALUES_DICT

"""A .py with all miscellaneous functions"""


def print_all_in_list(list_to_be_printed):
    """Void function for printing off each item in a list on a new line.
    Does not return anything"""
    for item in list_to_be_printed:
        print(item)


def calculate_gematria(text):
    """Takes a hebrew input and returns a int with the gamatria.
    :return int
    """
    value = 0
    for character in text:
        if character in VALUES_DICT:
            value += VALUES_DICT[character]
    return value


def output_list_to_file(list_to_be_outputed, filename, text_before="", text_after=""):
    """A function to output a list to a file.
    The output is csv, so if the end of file = .csv it will be a valid csv file.
    Does not return anything"""
    file = open(filename, "w", encoding="utf-8")

    if text_before != "":  # So a blank extra line is not printed at the top
        file.writelines(text_before)

    file.writelines("Book, Chapter, Verse, Gamatria, value\n")  # headers
    for verse in list_to_be_outputed:
        file.writelines(repr(verse))
        file.writelines("\n")  # just a line in between

    if text_before != "":  # As to not print a blank verse
        file.writelines(text_after)

    file.close()
