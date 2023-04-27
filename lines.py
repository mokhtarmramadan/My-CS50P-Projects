import sys

lines = []

# Initialize the line counter
counter = 0

# Exit the programe with a usage message if we have more than two cml argument 
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Exit the programe with a usage message if we have less than two cml argument 
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# Exit the programe with a usage message if the file name didn't end with .py
elif not sys.argv[1].endswith('.py'):
    sys.exit("Not a Python file")

else:
    try:
        # Open the file in the read mode as "file"
        with open(sys.argv[1], "r") as file:
            # Iterate through all the lins in file and raise the counter one every time
            for line in file:
                lines.append(line.rstrip())

    # If the file doesn't exist exite with a usage message
    except FileNotFoundError:
        sys.exit("File does not exist")

# Print the numbers of lines we counted exculding the comments and the spaces
for line in lines:
    if line == '' or line.startswith("#"):
        continue
    else:
        counter += 1

print(counter)