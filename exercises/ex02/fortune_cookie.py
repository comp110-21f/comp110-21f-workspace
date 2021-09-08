"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730518679"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

choice: int = int(input("How many letters are in your name?: "))

print("Your fortune cookie says...")

if choice < 6:
    if choice < 4:
        print("You will meet the person of your dreams")
    else:
        print("Luck will strike you when you least expect it")
else:
    if choice < 8:
        print("A person you don't know will help you in a significant way")
    else:
        print("Your focus, strength, and happiness will be at an all time high")

print("Now, go spread positive vibes!")