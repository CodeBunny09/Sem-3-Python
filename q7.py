"""
7. Write a program for filter() to filter only even numbers from a given list.
"""

l = [1, 23, 4, 3, 5, 6, 4, 3, 56, 7, 54, 3, 24, 5, 8, 9, 10, 23, 43, 22]
print(f'Original list: {l}')

filtered = filter(lambda x: not bool(x % 2), l)
print(f'Filtererd list: {list(filtered)}')
