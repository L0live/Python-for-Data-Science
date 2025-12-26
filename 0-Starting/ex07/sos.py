import sys


def main():
    """Convert text to Morse code.
    
    Accepts a single string argument containing alphanumeric characters and spaces.
    Converts each character to Morse code and prints the result.
    """
    assert len(sys.argv) == 2 and all((c.isdigit() or c.isupper() or c.islower() or c == ' ') for c in sys.argv[1]), "the arguments are bad"

    MORSE_CODE_DICT = {' ': '/', 'A': '.-', 'B': '-...',
                        'C': '-.-.', 'D': '-..', 'E': '.',
                        'F': '..-.', 'G': '--.', 'H': '....',
                        'I': '..', 'J': '.---', 'K': '-.-',
                        'L': '.-..', 'M': '--', 'N': '-.',
                        'O': '---', 'P': '.--.', 'Q': '--.-',
                        'R': '.-.', 'S': '...', 'T': '-',
                        'U': '..-', 'V': '...-', 'W': '.--',
                        'X': '-..-', 'Y': '-.--', 'Z': '--..',
                        '1': '.----', '2': '..---', '3': '...--',
                        '4': '....-', '5': '.....', '6': '-....',
                        '7': '--...', '8': '---..', '9': '----.',
                        '0': '-----'}

    entry = sys.argv[1].upper()

    encrypted = ""
    for c in entry:
        encrypted += MORSE_CODE_DICT[c] + ' '

    print(encrypted[:-1])


if __name__ == "__main__":
    main()
