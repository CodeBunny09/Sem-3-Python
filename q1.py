# q1: Python data types

# Numeric data types
a = 5   #Integer
f = 4.23    #Float
c = 7 + 22j     #Complex number

#String data type
s = "Hello World!!!"

#Sequence types
l = ['a', "Hello", 23, 4.7, 7+5j]   #List
t = ('a', "Hello", 23, 4.7, 7+5j)   #Tuple
r = range(10)   #Range: This creates a list from one 0 to 9

#Binary data types
b = bytes(23)   #Bytes
ba = bytearray("Hello", encoding="UTF-8")   #Bytearray
mv = memoryview(ba)     #Memoryview: This datatype takes buffer objects like bytes, bytearrays, etc

#Mapping data types
d = {
    1: "Tea",
    2: "Coffee",
    3: "Bread",
    4: "Egg"
}   #Dictionary: This maps keys with values

#Boolean data type
tr = True
fa = False

#Set data types
se = {22, 22, 34, 54, 67, 67, 81, 2, 3, 2, 5, 1}    #Set
fs = frozenset(se)  #Frozenset

#Taking all the objects in a list to print them all

all = [a, f, c, s, l, t, r, b, ba, mv, d, tr, fa, se, fs]

for i in all:
    print(f'Datatype: {type(i)}')
    print(f'Value:\n{i}')
    print("\n\n")
