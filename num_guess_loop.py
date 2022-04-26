#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 24, 2022
# This program generates a random number between 0 and 9
# It then uses a while TRUE loop  to keep asking the user
# to guess the number until they guess correctly.


import random


def main():
    # generate the random number
    random_number = random.randint(0, 9)

    while True:
        # Get the user input as a string
        user_input_string = input("Guess a random number between 0 and 9: ")
        print("")
        try:
            # cast the user number to int
            user_input = int(user_input_string)

            if user_input == random_number:
                print("That is correct!")
                break
            else:
                print("Incorrect number! Try Again!")
                print("")
                continue

        except Exception:
            print("That is not a number!! Try Again!")
            print("")


if __name__ == "__main__":
    main()
