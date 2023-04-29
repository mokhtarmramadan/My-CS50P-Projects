from sys import exit, argv
from PIL import Image, ImageOps

def main():

    check_argv()
    
    try:
        image = Image.open(argv[1])

    except FileNotFoundError:
        exit("file not found")
    
    # Open the shirt "mask" image and if we can't exsit the programe with a usage message           
    shirt = Image.open("shirt.png")
    

    # Get the size of the shirt "mask" and crop the input image to fit the mask
    size = shirt.size
    new_image = ImageOps.fit(image, size)

    # Paste the shirt image on our resized input image
    new_image.paste(shirt, shirt)

    # Save the new image
    new_image.save(argv[2])


def check_argv():
    # Exit the programe with a usage message if we have more than three cml argument 
    if len(argv) > 3:
        exit("Too many command-line arguments")

    # Exit the programe with a usage message if we have less than three cml argument 
    elif len(argv) < 3:
        exit("Too few command-line arguments")

    # Make sure that the input file has one of the following formates 
    elif not argv[1].endswith(".jpeg") and not argv[1].endswith(".jpg") and not argv[1].endswith(".png"):
        exit("Invalid input")

    # Make sure that the output file has one of the following formates 
    elif not argv[2].endswith(".jepg") and not argv[2].endswith(".jpg") and not argv[2].endswith(".png"):
        exit("Invalid output")

    # Exit the programe if the input and the output file don't have the same extensions
    elif argv[1].endswith(".jpeg"):
        if not argv[2].endswith(".jpeg"):
            exit("Input and output have different extensions")
        
    elif argv[1].endswith(".jpg"):
        if not argv[2].endswith(".jpg"):
            exit("Input and output have different extensions")

    elif argv[1].endswith(".png"):
        if not argv[2].endswith(".png"):
            exit("Input and output have different extensions")
    else:
        return True
    
if __name__ == '__main__':
    main()