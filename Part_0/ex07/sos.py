import sys


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'    # Resets all attributes
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/",
}


def main():
    """
    Main function, which encode characters into Morse
    :return: Morse
    """
    try:
        if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
            raise AssertionError(f"{Colors.FAIL}AssertionError: the arguments are bad{Colors.ENDC}")
        text = sys.argv[1]
        encoded = ""
        for char in text.upper():
            if char in NESTED_MORSE:
                encoded += NESTED_MORSE[char] + " "
            else:
                raise AssertionError(f"{Colors.FAIL}AssertionError: Invalid character in input text{Colors.ENDC}")
        print(encoded)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
