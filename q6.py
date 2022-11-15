"""
6. Write a python program to print a number is positive/negative using if-else
"""

n = int(input("Enter an integer: "))

if n < 0:
    print("The number is negative")
elif n > 0:
    print("The number is positive")
elif n == 0:
    print("The number is 0")