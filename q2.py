"""
Create a list and perform the following methods
1) insert() 2) remove() 3) append()
4) len() 5) pop() 6) clear()
"""

#Creating a list
l = [2, 3, 1, 4, 5, 4, 1, 6, 8]
print("Created a list: " + str(l) + "\n")

#1: Insert
l.insert(3, 45)     #First argument: Index, Second argument: Element. This inserts the element at the given position
print("After 'l.insert(3, 45)' : " + str(l) + "\n")

#2: Remove
l.remove(3)     #Removes the first occurance of the element
print("After 'l.remove(3)' : " + str(l) + "\n")

#3: Append
l.append(34)    #Inserts one element to the end of the list
print("After 'l.append(34)' : " + str(l) + "\n")

#4: Len
a = len(l)      #Gives the length of the list
print("'len(l)' : Gives the length of the list: " + str(a))

#5: Pop
l.pop()     #Removes an element from the end of the list
print("After 'l.pop()' : " + str(l) + "\n")

l.pop(4)    #Removes an element at the given index
print("After 'l.pop(4)' : " + str(l) + "\n")

#6: Clear
l.clear()   #Removes all the element in the list
print("After 'l.clear()' : " + str(l) + "\n")
