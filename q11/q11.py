"""
11. Write a program to count frequency of characters in a given file
"""

count = {}

with open("q11.txt", "r") as file:
    st = file.read()

    for i in st:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] = count[i] + 1


print("Count of each characters appearing in the string:\n\n")

for k, v in count.items():
    print(f'Character: {k} ({v})')