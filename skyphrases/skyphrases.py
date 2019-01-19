def check_duplicates(passphrase):
    """
    Function converts string into a list and compares it's length
    with length of set created from this list.
    """
    splitted_phrase = passphrase.split()
    if len(splitted_phrase) == len(set(splitted_phrase)):
        return True


def count_valid_phrases_in_file(source_file):
    """
    Function iterates through the file
    and checks each line if it's valid skyphrase
    """
    count = 0
    with open(source_file) as fn:
        for line in fn:
            if check_duplicates(line):
                count += 1
    return count
