import sys

def main():
    assert len(sys.argv) <= 2, "more than one argument is provided"

    if len(sys.argv) != 2 or not len(sys.argv[1]):
        print("What is the text to count?")
        string = input()
    else:
        string = sys.argv[1]
    print("The text contains", len(string), "characters:")
    print(sum(1 for c in string if c.isupper()), "upper letters")
    print(sum(1 for c in string if c.islower()), "lower letters")
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(sum(1 for c in string if c in punctuation), "punctuation marks")
    print(sum(1 for c in string if c.isdigit()), "digits")
    print(string.count(' '), "spaces")

if __name__ == "__main__":
    main()