import re
import os


# Crossplatform file path handling
source_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'skychallenge_accounting_input.txt'
    )


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


# Print the sum of integers in the file
if __name__ == '__main__':
    print(find_and_sum_integers_from_file(source_path))
