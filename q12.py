"""
12. Using a numpy module create an array and check the following: 1. Type of array 2. Axes of array 3. Shape
of array 4. Type of elements in array
"""

import numpy as np

arr = np.array([
    [[1, 2, 4, 3],
    [2, 4, 2, 6],
    [5, 1, 3, 2],
    [2, 1, 8, 9]],

    [[1, 3, 7, 5],
    [3, 1, 5, 9],
    [6, 1, 2, 8],
    [9, 0, 1, 5]],

    [[1, 3, 7, 4],
    [3, 1, 5, 6],
    [2, 1, 9, 8],
    [5, 1, 6, 4]],

    [[1, 9, 2, 1], 
    [2, 3, 1, 9],
    [5, 6, 7, 0],
    [1, 4, 7, 2]]
])

print(f'The array:-\n{arr}')

# 1: Type of the array
print(f'\n1: Type of array: {type(arr)}')

# 2: Axes of the array
print(f'\n2: Number of dimensions of the array: {arr.ndim}')
print(f'Sum of the array using axis = 0:\n{arr.sum(axis=0)}')
print(f'Sum of the array using axis = 1:\n{arr.sum(axis=1)}')
print(f'Sum of the array using axis = 2:\n{arr.sum(axis=2)}')

# 3: Shape of the array
print(f'\n3: The shape of the array is: {arr.shape}')

# 4: Type of elements in the array
print(f'\n4: Type of elements: {arr.dtype}')