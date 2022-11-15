"""
5. Write a program to create a menu with the following options
1. TO PERFORM ADDITITON 2. TO PERFORM SUBTRACTION
3. TO PERFORM MULTIPICATION 4. TO PERFORM DIVISION
Accepts users input and perform the operation accordingly. Use functions with arguments.
"""

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

option = int(input("Options:\n1: Addition\t2: Subtraction\n3: Multiplication\t4: Division\n5: Exit\n\nChoose your option: "))

if option == 5:
    print("Bye...")
elif option > 5:
    print("\nPlease enter a valid option...")
else:
    a = int(input("\nEnter value for 'a': "))
    b = int(input("Enter value for 'b': "))

    match option:
        case 1:
            print(f'\na + b = {add(a, b)}')
        case 2:
            print(f'\na - b = {sub(a, b)}')
        case 3:
            print(f'\na * b = {mul(a, b)}')
        case 4: 
            print(f'\na / b = {div(a, b)}')
