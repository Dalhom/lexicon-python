""""

You can actually make a simple command line game. You could put together everything
you've learned so far about Python. The game goes like this:

1. The computer will think of 3 digit number that has no repeating digits.
2. You will then guess a 3 digit number
3. The computer will then give back clues, the possible clues are:
Close: You've guessed a correct number but in the wrong position
Match: You've guessed a correct number in the correct position
Nope: You haven't guess any of the numbers correctly
4. Based on these clues you will guess again until you break the code with a
perfect match!

There are a few things you will have to discover for yourself for this game!
Here are some useful hints:

Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

Another hint:
guess = input("What is your guess? ")
print(guess)

Think about how you will compare the input to the random number, what format
should they be in? Maybe some sort of sequence?

"""

    

import random

digits = list(range(10))
random.shuffle(digits)
# print('My digits are: ',digits[:3])

user_input = input("Guess three numbers up to 9, separated by space? ")
guess_list = list(map(int, user_input.split()))

print("Your guess is: ", guess_list)

while digits[0] != guess_list[0] or digits[1] != guess_list[1] or digits[2] != guess_list[2]:



    clues = []
    for i in range(3):  # loop through each index in the guess
    
        if guess_list[i] == digits[i]:
            clues.append("Match")
    
        elif guess_list[i] in digits:
            clues.append("Close")
    
        else:
            clues.append("Nope")

    print(clues)

    user_input = input("Guess three numbers up to 9, separated by space? ")
    guess_list = list(map(int, user_input.split()))

print("You've broken the code with a perfect match!")

