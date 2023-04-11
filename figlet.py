# import pyfiglet and sys module 
import pyfiglet
import sys
import random 

   
# Check for CMD errors
if len(sys.argv) == 3 and sys.argv[1] in ["-f"]:
    try:
        # Asking the user for an input
        text = input("Input: ")
        # Printing the input with the font style  
        result_2 = pyfiglet.figlet_format(text, font= sys.argv[2])
        print(result_2)
        
    # If the font doesn't exist in figlet exit    
    except:
        sys.exit("Invalid usage")
    
# Check if the useer didn't provid any CMD arguments
elif len(sys.argv) == 1:
    # Asking the user for an input
    text = input("Input: ")  
    # Putting all the existing fonts of pyfiglet into a list
    all_fonts = pyfiglet.FigletFont.getFonts()
    # Randomly choosing a font name out of the font list
    new = random.choices(all_fonts)
    # Print the result
    result_0 = pyfiglet.figlet_format(text, font= new[0])
    print(result_0)

# Exiting if we have any other number of CMD arguments
else: 
    sys.exit("Ivalid usage")