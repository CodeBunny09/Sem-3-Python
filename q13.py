"""
13. Write a python program to concatenate the dataframes with two different objects
"""

import pandas as pd

data = {
    "Name": ["Jack", "Harley", "Peter", "Travis", "Trenton"],
    "Age": [20, 19, 22, 18, 20]
}

data2 = {
    "Name": ["Linsdey", "Elliot", "Angela", "Darlene", "Shayla"],
    "Age": [18, 20, 20, 18, 19]
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)


print(f'First Dataframe: "df1":-\n{df}')
print(f'Second Dataframe: "df2":-\n{df2}')

df3 = pd.concat([df, df2], axis=0)
df4 = pd.concat([df, df2], axis=1)

print(f'\nAfter concatenating "df1" with "df2" along axis = 0\n{df3}')
print(f'After concatenating "df1" with "df2" along axis = 1\n{df4}')