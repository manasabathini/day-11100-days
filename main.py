print("How many seconds are there in a year?")

minute = 1 * 60
hour = 60 * 60
day = 24 * 60 * 60
sLY = 366 * 24 * 60 * 60
sRY = 365 * 24 * 60 * 60

year = int(input("please enter the year: "))
if (year % 400 == 0) and (year % 100 == 0):
   print("The year is leap year. Number of seconds in a leap year: ", sLY)
elif (year % 4 ==0) and (year % 100 != 0):
  print("The year is leap year. Number of seconds in a leap year: ", sLY)
else:
  print("The year has 365 days. So number of seconds in a regular year: ", sRY)