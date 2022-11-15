"""
14. Write a python code to read a csv file using pandas module and print the first and last five lines of a file.
"""
# The dataset used here was downloaded from https://www.kaggle.com/datasets/devzohaib/eligibility-prediction-for-loan


import pandas as pd

df = pd.read_csv("q14.csv", on_bad_lines='skip', index_col="Loan_ID")

print(f'First five lines of the dataframe:\n{df.head()}')
print(f'\nLast five lines of the dataframe:\n{df.tail()}')