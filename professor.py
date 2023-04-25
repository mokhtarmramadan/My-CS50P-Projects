import random

# initialize level
level = 0

def main():
    # level user provided
    level = get_level()

    # Dictionary of two values 1-equation 2-the answer
    dict = generate_integer(level)

    # counters for the correct and the incorrect answers
    correct_answers = 0
    wrong_answers = 0

    #  Reprompting if the input is not an int    
    while True:        
            # Prompting for 10 times
            for l in range(10):
                
                # Try to get an int from the user 
                try:
                    if int(input(dict["equation"])) == int(dict["answer"]):
                        # If the input is an int and it quals the answer in the dictionary we raise the 
                        # correct_answers counter one
                        correct_answers += 1
                        
                        # Generate a new dict once the user answered correctly
                        dict = generate_integer(level)

                    # If the user answers incorrectly it should print EEE for three tries, set the counter
                    # to zero, print the correct answer and gererate a new dictionary 
                    elif wrong_answers >= 2:
                        wrong_answers = 0
                        print("EEE")
                        print(f"{dict['equation']} = {dict['answer']} ")

                        # Generating the random numbers for both left hand and right hand side
                        dict = generate_integer(level)


                    # Break the loop once we print the 10th equation
                    elif l == 9:
                        break
                    # Raise the wrong_answers counter by one if it's a wrong answer and print EEE
                    else:
                        wrong_answers += 1
                        print("EEE")

                # If the answer was not an int; raise the wrong_answers counter by one, check if the counter
                # exceeded 3 times if yes set it to 0, print EEE, print the correct
                # answer and generate a new dict
                except:
                    wrong_answers +=1
                    if wrong_answers > 2:
                        wrong_answers = 0
                        print("EEE")
                        print(f"{dict['equation']} = {dict['answer']}")

                        # generating the random numbers for both left hand and right hand side
                        dict = generate_integer(level)
                    
                    else:
                        print("EEE")

            # After prompting 10 questions we return the correct_answers counter as a result and break
            print(correct_answers)
            break



def get_level():
    # Prompt the user for a int level from 1 to 3
    i = 0
    while True:
        try:    
            i = int(input("level: "))
            if i in [1, 2, 3]:
                return i
            
            # If the user input was anything but 1 or 2 or 3 reprompt again
        except ValueError:
            continue



def generate_integer(level):

    # If the leave we got is 1 we should generate a one digit int in the left hand and the 
    # right had side of the equation and following the same logic if it was 2 or 3
    if int(level) == 1:
        LHS = str(random.randint(0, 9))
        RHS = str(random.randint(0, 9))
    elif int(level) == 2:
        LHS = str(random.randint(10, 99))
        RHS = str(random.randint(10, 99))
    else:
        LHS = str(random.randint(100, 999))
        RHS = str(random.randint(100, 999))
    
    # the real answer we should compare against 
    real_answer = int(LHS) + int(RHS)  

    # Store the equation and the answer in a dictionary structure and return it
    dict = {"equation" : f"{LHS} + {RHS} = ", "answer" : real_answer}
    
    return dict


if __name__ == "__main__":
    main()