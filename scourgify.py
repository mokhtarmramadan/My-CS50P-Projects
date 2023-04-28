import csv
import sys

# Exit the programe with a usage message if we have more than three cml argument 
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Exit the programe with a usage message if we have less than three cml argument 
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
                
# Exit the programe with a usage message if any of the files name didn't end with .csv               
elif not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):
    sys.exit("Not a CSV file")

else:
    # Try to open the input file and read it with a DictReader
    try:
        with open(sys.argv[1], 'r') as file:
            reader = csv.DictReader(file)

            # Iterate through the file and split the name part by comma and store them in two variables
            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]

                # Open the output file in append mode and append to it a dict with the variables we got
                # from the first file 
                with open(sys.argv[2], 'a') as after:
                    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                    writer.writerow({"first": first, "last": last, "house": house})
    
    # If any of the files don't exist exit with a usage message
    except FileNotFoundError:
        sys.exit("File does not exist")