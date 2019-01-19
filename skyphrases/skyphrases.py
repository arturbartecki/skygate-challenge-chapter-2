def check_duplicates(passphrase):
    """
    Function converts string into a list and compares it's length
    with length of set created from this list.
    """
    splitted_phrase = passphrase.split()
    if len(splitted_phrase) == len(set(splitted_phrase)):
        return True
