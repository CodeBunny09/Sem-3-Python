"""
10. Write a program to count the numbers of characters in the string and store them in a dictionary data
structure
"""

count = {}

st = input("Enter a string: ")

for i in st:
    if i not in count.keys():
        count[i] = 1
    else:
        count[i] = count[i] + 1

print("Count of each characters appearing in the string:\n\n")

for k, v in count.items():
    print(f'Character: {k}\tCount: {v}')