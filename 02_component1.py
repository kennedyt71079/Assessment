import random


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

# Main Routine
low = intcheck("Please choose a low number - ")
high = intcheck("Please choose a high number - ", low + 1)

random1 = random.randint(low, high)
random2 = random.randint(low, high)

print(random1)
print(random2)