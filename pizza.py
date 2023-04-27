# Import the tabulate lib that will format the list as table
from tabulate import tabulate
import sys

# List to store the values we'll get from the CSV file
table = []

# Exit the programe with a usage message if we have more than two cml argument 
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Exit the programe with a usage message if we have less than two cml argument 
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
                
# Exit the programe with a usage message if the file name didn't end with .csv               
elif not sys.argv[1].endswith('.csv'):
    sys.exit("Not a CSV file")

else:
    try:
        # Open the file in the read mode as "file"
        with open(sys.argv[1], "r") as file:
            # Iterate through it and add every word splited by comma to the table list
            for line in file:
                table.append(line.rstrip().split(","))

    # If the file doesn't exist exite with a usage message
    except FileNotFoundError:
        sys.exit("File does not exist")

# Create the header list which is the first line in the csv file
headers = table[0]
# Delete the first line of the csv file from table list so it won't be duplicate when we print
del table[0]
# Print the table using the tabulate lib and passing to it the table and the headers list
print(tabulate(table, headers, tablefmt="grid"))