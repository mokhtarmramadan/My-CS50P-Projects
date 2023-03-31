def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
     # Check for the first, seconde and the third requirement
    if len(s) > 1 and len(s) < 7:
        if s[0].isalpha() and s[1].isalpha():
            for i in range(len(s)):
                if not s[i].isalpha() and not s[i].isdigit():
                    return False
    else:
        return False

    # Checking if the the plate is a middle-number case or if the numbers starts with 0
    for j in range(1, len(s) - 1):
        if s[j].isdigit() and not s[j + 1].isdigit() or s[j] == '0' and s[j - 1].isalpha():
            return False
    return True


if __name__ == "__main__":
    main()