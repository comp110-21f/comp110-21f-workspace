"""Repeating a beat in a loop."""

__author__ = "730518679"


beat: str = str(input("What beat do you want to repeat?: "))

times: int = int(input("How many times do you want to repeat it?: "))

t: int = 0
b: str = ""

if times < 0:
    print("No beat...")
else:
    while t < times: 
        if t < times:
            b = b + beat + " "
            t = t + 1
        else:
            b = b
    print(b)