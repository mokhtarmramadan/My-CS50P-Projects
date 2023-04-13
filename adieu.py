# Import the inflect lib to join my list together
import inflect

# Create a p varibale for the inflect engine
p = inflect.engine()

def main():


    # Create an empty list for the user input
    mylist = []

    # Prompting the user for inputs till he enters ctr+d
    while True:
        try:
            # Trying to append every input in our list unless we have an exception 
            name = str(input("Name: "))
            mylist.append(name)

            # If we have an exceptian we'll go ahead and print the list with the p.join method 
            # and break out of the loop
        except:
            print(output(mylist))
            break
        
# Created a function to make my code more testable
def output(mylist):            
    return f"Adieu, adieu, to {p.join(mylist)}" 

main()