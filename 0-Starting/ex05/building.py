from sys import argv


def main():
    """Analyze and count different character types in a text string.

    Accepts text via command line argument or stdin input.
    Counts upper/lower letters, punctuation marks, digits, and spaces.
    """
    assert len(argv) <= 2, "more than one argument is provided"

    try:
        if len(argv) != 2 or not len(argv[1]):
            print("What is the text to count?")
            string = input()
        else:
            string = argv[1]
        print("The text contains", len(string), "characters:")
        print(sum(1 for c in string if c.isupper()), "upper letters")
        print(sum(1 for c in string if c.islower()), "lower letters")
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        print(sum(1 for c in string if c in punctuation), "punctuation marks")
        print(sum(1 for c in string if c.isdigit()), "digits")
        print(string.count(' '), "spaces")
    except EOFError:
        print("Nothing... ok, bye")


if __name__ == "__main__":
    main()
