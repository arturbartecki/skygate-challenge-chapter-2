import re


def find_and_sum_integers_from_file(source_file):
    """
    Function takes as an argument text file
    and returns sum of every integer in that file
    """
    with open(source_file, "r") as fn:
        filtered_integers = [
            int(chunk) for chunk in re.findall(r'-?\d+', fn.read())
            ]
        return(sum(filtered_integers))
