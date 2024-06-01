import sys
import string


def count_characters(text: str) -> dict:
    """
    This function count characters in the provided text

    :param text: Input string from user
    :return: Dictionary with counts of lower-, upper-case letters, punctuation,
    spaces and digits
    """

    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0
    }

    # Oh my, look, this is the functions!
    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char in string.punctuation:  # That's why I need string, to catch special symbols
            counts["punctuation"] += 1
        elif char.isspace():
            counts["spaces"] += 1
        elif char.isdigit():
            counts["digits"] += 1

    return counts


def main():
    """
    Main function. Here's checks for args, input and output handle

    :return: Count of all characters in provided string
    """
    try:
        if len(sys.argv) == 1:
            text = input("What is the text to count? \n")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("more than one argument is provided")

        counts = count_characters(text)
        total_number_to_output = len(text)

        print(f"The text contains {total_number_to_output} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
