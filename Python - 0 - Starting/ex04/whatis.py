import sys

assert len(sys.argv) <= 2, "more than one argument is provided"

assert sys.argv[1].isdigit(), "argument is not an integer"

if int(sys.argv[1]) % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")