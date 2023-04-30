# Import sys to use exist
import sys

# Initialize a list for user input and a new list with no duplicates 
grocery = []
new_list = []

# Reprompt the user for input till they enter ctr+d
while True:
    # If the input is not ctr+d append user input into the grocery list as a dict where it's a name and it takes a defualt
    # value of one
    try:
        item = input("")
        grocery.append({"key" : item.upper(), "value" : 1 })
    
    # If the input is ctr+d
    except:
        # Inatialize a coutner for to determine the start range of the list in the second loop
        counter = 0
        # Iterate through tha main list
        for item in grocery:
            # Inatailize a value counter with a start value of one
            value = 1
            counter +=1
        
            # Loop starting form counter to the end of the grocery list
            for i in grocery[int(counter):]:
                # If the name exist more than once remove the replicates and raise the value counter and append the resualts
                # in the new list
                if item["key"] == i["key"]:
                    grocery.remove({"key" : i["key"], "value" : i["value"] })
                    value += 1

            new_list.append({"key" : item["key"], "value" : value})

        # Print the sorted keys and values of the new list
        for dict in sorted(new_list, key=lambda item: item["key"]):
            print(dict["value"], dict["key"])

        # Exit the program
        sys.exit()