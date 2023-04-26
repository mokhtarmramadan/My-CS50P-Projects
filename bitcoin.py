import requests
import json
from sys import argv, exit

def main():
    # Check if we only have 2 argv not more or less
    if len(argv) != 2:
        exit("Missing command-line argument")

    # Make sure that the second argv is a float
    if isfloat(argv[1]):
        exit("Command-line argument is not a number")

    
    try:
        # Try to get request from the browser
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Store the json file we got as a variable
        objekt = request.json()

        # Store a dictionary in that json file called 'bpi' in a new variable
        dict_of_dicts = objekt['bpi']

        # In that dict there's another dict called USD that we stored in a new variable
        child_dict = dict_of_dicts['USD']

        # In the last dict we got we need to get the value of the keyword 'rate' and store it as price
        price = child_dict['rate']

        # Using the replace function to remove commas so we can treat the price as a float
        price = price.replace(",", "")

        # Multiply the current price of the bitcoin by the number of bitcoins user enters
        result = float(price) * float(argv[1])
        
        # Print the result in the USD format
        print(f"${result:,.4f}")
    
    # Exit if we face any request exceptions    
    except requests.RequestException:
        exit

# isfloat returns flase if the num is a float and true if it was something else
def isfloat(num):
    try:
        float(num)
        return False
    except:
        return True


if __name__ == '__main__':
    main()