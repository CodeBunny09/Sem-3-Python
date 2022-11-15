"""
9. Write a python program to add some days to your present date and print the date added
"""

import datetime

today = datetime.date.today()
print(f'Today: {today}')

n = int(input("Enter the number of days you want to add: "))

thatDay = today + datetime.timedelta(days=n)
print(f'After adding {n} days, the date is: {thatDay}')
