#1.2 write a program that determines whether a year enter the user is a leap year or not using ifelif-else statements
"""
year % 4 ==0&
year % 100!=0/
year % 400==0
"""


def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0):
    return True
  else:
    return False


year = int(input("enter a year :"))
if isleapyear(year):
  print('{} is a leapyear.'.format(year))
else:
  print('{} is not a leapyear.'.format(year))
