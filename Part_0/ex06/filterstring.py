import sys
from ft_filter import ft_filter


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


def main():
    """
    Main function to filter words from a string based on their length.
    :return: result of ft_filter
    """
    try:
        assert len(sys.argv) == 3, f"{Colors.FAIL}AssertionError: the arguments are bad{Colors.ENDC}"
        S = str(sys.argv[1])
        N = int(sys.argv[2])
    except (AssertionError, ValueError) as e:
        print(e)
        return

    # Lambda-function for filtering the words, which length more than N
    filter_func = lambda word: len(word) > N
    words = S.split()
    filtered_words = [word for word in ft_filter(filter_func, words)]

    print(filtered_words)


if __name__ == "__main__":
    main()
