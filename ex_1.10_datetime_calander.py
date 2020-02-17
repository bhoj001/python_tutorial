import datetime
datetime_object = datetime.datetime.now() # Now date and time
print(datetime_object)

current_date= datetime.date.today() # if you want to print only date(and not time)
print(current_date) 

#  Date object to represent a date

# 
d = datetime.date(2020, 4, 13)
print("custom date =",d)

# date object of today's date
today = datetime.date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

"""
Getting calendar for a month
The calendar module gives a wide range of methods to play with yearly and monthly calendars. Here, 
we print a calendar for a given month ( Jan 2020 ) −
"""

import calendar

cal = calendar.month(2020, 1)
print("Here is the calendar:")
print(cal)

# c2 = calendar.February # gives number january = 1, feburary = 2 and so on 

# printing annual calander in 3 columns
# docs: https://www.wikipython.com/modules/407-2/
import calendar
year = 2020
c=calendar.TextCalendar()
c.pryear(year)