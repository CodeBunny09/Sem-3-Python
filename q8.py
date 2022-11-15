"""
8. Write a python program to print date, time for today and now
"""

import datetime
import pytz #This is for setting timezone as time varies from place to place

today = datetime.date.today()
now = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
cTime = now.strftime("%H:%M:%S")

print(f'Current date: {today}\nCurrent time: {cTime}')