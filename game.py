import random

# Creating two variables for the user prompt
level = 0
guess = 0

# Making sure that the level input is a positive int
while True:
        
    # break out of the loop if the number is a positive int
    try:
        level = int(input("Level: "))

        if level > 0:
            break
    except:
        continue

# Generating a random number by randrange and passing "level" input as a range
random_number = random.randrange(1, level + 1)

# Making sure that the guess input is a positive int
while True:
            
    try:
        # Try to get an positive int from the user
        guess = int(input("Guess: "))
        if guess > 0:

            # If the number is a positive int then move forward else keep reprompting the user for
            # a positive int 
            if random_number == guess:

                # if the random number we genrated equals to user's guess then print "Just right!" and
                # break out of the loop
                print("Just right!")
                break
        
            elif random_number > guess:

                # If the guess is smaller print "Too small!" and continue in the loop
                print("Too small!")

            else:

                # Else if it's larger print "Too large!" and continue the loop as well 
                print("Too large!")
    except:
        # Continue reprompting if the input wasn't a positive int
        continue

