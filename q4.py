"""
4. Create a dictionary and apply the following methods
1) Print the dictionary items 2) access items 3) use get()
4)change values 5) use len()
"""

d = {
    1: "Ferrari",
    2: "Buggati",
    3: "Toyoya",
    4: "Nissan",
    5: "Honda",
    6: "Volkswagen",
    7: "Hyundai"
}

# 1: Print dictionary items
print("1: Items in the dictionary: ")
for i in d.items():
    print(i)

# 2, 3: Access items and Use get()
print("\n2, 3: Accessing items and using 'get()'")

k = int(input("Enter the key of the value you want to access: "))

if k in d.keys():
    v = d.get(k)
    print(f'Key: {k}\tValue: {v}')
else:
    print("Key not in dictionary!")

# 4: Change values
print("\n4: Changing values...")
d[4] = "Mitbushi"
print(d)

# 5: Use 'len()'
print("\nUse 'len()': ")
l = len(d)
print(f'Length of the dictionary is: {l}')


