"""This program sets two variables equal to a number and then compares them using various relational operators."""

__author__ = "730518679"

x: str = input("What is the first number? ")
y: str = input("What is the second number? ")
print("Left-hand side:", x)
print("Right-hand side:", y)
print(x, "<", y, "is", x < y)
print(x, ">=", y, "is", x >= y)
print(x, "==", y, "is", x == y)
print(x, "!=", y, "is", x != y)