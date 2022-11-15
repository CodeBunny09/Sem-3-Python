"""
3. Create a tuple and perform the following methods
1) Add items 2) len() 3) check for item in tuple 4)Access items
"""

tup = (1, 4, 5, 3, 2)
print(tup)

# 1: Add items
try:
    tup = tup + 5
except Exception as e:
    print("\n1: Tuples are immutable, items can not be added to it.")

print(tup)

# 2: len()
l = len(tup)
print(f'\n2: The length of the tuple is: {l}')

# 3: Check for an item in tuple
n = int(input("\n3: Enter a number to search in the tuplpe: "))
if n in tup:
    pos = tup.index(n)
    print(f'Position of "{n}" in the tuple is: {pos}')
else:
    print("Element not present.")

# 4: Access items
print("\n4: Accessing items: ")
count = 0
for i in tup:
    print(f'Position: {count}\tElement: {i}')
    count += 1

