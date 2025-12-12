import sys
from ft_filter import ft_filter

def main():
    assert len(sys.argv) == 3 and sys.argv[2].isdigit(), "the arguments are bad"

    words = sys.argv[1].split()

    result = ft_filter(lambda word: (len(word) > int(sys.argv[2])), words)

    print(result)

if __name__ == "__main__":
    main()