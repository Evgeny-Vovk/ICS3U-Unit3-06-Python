# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Unit3-03.py File, learning try...catch... statements in python.

import random


def main():

    # input and variables
    random_number = random.randint(0, 9)
    guess_number = input("Guess the number from 0 to 9: ")

    # process and output
    print("")
    try:
        if int(guess_number) == random_number:
            print("You guessed right.")
        else:
            print("You guessed wrong, the number was {0}.".format(random_number))
    except ValueError:
        print("invalid input, {0} does not fit the requirements.".format(guess_number))
        print("Please try again and input a whole number between 0 and 9.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
