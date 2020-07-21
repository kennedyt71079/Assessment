import random

# Number Checker Fucntion
def intcheck(question, low=None, high=None):

    # Sets up error messages
    if low is not None and high is not None:
        error = "Please enter an interger between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# Welcome Text
print("Welcome to the addition quiz!!! :)")
print()
print("The game generates 2 random numbers for each question,")
print("The low number is how low the number is generated,")
print("The High number is how high the number is generated,")
print("And the questions are how many equations you will be asked!")
print("Please answer the questions below to start the game :)")
print()

# Main Routine
low = intcheck("Please choose a low number - ")
high = intcheck("Please choose a high number - ", low + 1)
questions = intcheck("How many questions do you want to play? ")
print("Good Luck, Have Fun!")
questions_answered = 0
right = 0
wrong = 0

# Generates random numbers, adds them together, and loops from here
while questions_answered < questions:
    random1 = random.randint(low, high)
    random2 = random.randint(low, high)
    answer = random1+random2

    # Generates the Equation
    print()
    guess = intcheck("What is {} + {} = ".format(random1, random2))

    # Checks to see if the answer is correct
    if guess == random1 + random2:
        print("Congratulations, That is correct!")
        right += 1
        print("You have gotten {} Correct and {} Wrong".format(right, wrong))
    else:
        print("Sorry, That is incorrect, The answer was {}".format(answer))
        wrong += 1
        print("You have gotten {} Correct and {} Wrong".format(right, wrong))
    questions_answered += 1

    # Checks to see how many questions are left
    if questions_answered == questions:
        continue

# End game text
print()
print("You have gotten to the end of the quiz")
print("You got {} out of {} Questions right!".format(right, questions))
