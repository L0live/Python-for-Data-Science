from sys import argv
from ft_filter import ft_filter


def main():
    """Filter words from a string based on minimum length.

    Expects two arguments: a string and a minimum word length (integer).
    Prints list of words longer than the specified length.
    """
    assert len(argv) == 3 and argv[2].isdigit(), "the arguments are bad"

    words = argv[1].split()

    result = ft_filter(lambda word: (len(word) > int(argv[2])), words)
    print(result, '\n')


if __name__ == "__main__":
    main()
