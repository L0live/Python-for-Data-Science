from sys import argv

assert len(argv) <= 2, "more than one argument is provided"

if len(argv) == 2:
    arg = argv[1]
    if arg[0] == '-':
        arg = arg[1:]
    assert arg.isdigit(), "argument is not an integer"

    if int(argv[1]) % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
