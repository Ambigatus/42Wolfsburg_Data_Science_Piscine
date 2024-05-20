import sys

# Counter. ffs, whyy??
arg_count = 0
for arg in sys.argv:
    arg_count += 1

# Start. Checking the number of argh. If one, go on
if arg_count == 2:
    arg = sys.argv[1]
    try:
        num = int(arg)
        # Check if number is int
        assert num.__class__ == int, "AssertionError: Argument is not an integer"
        if num % 2 == 0:  # Odd or Even?
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: Argument is not an integer")

# Check for more than 2 argh
elif arg_count > 2:
    print("AssertionError: more than one argument is provided")

# If we do not have argh
else:
    pass
