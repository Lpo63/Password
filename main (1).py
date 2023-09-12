#leap year

""
year % 4==0&
year%100!=0/
year%400==0

""
def is leap year(year):
  if(year%4==0and year%100!=0)oryear%400==0:
   return true
else:
    return False

year=int(input("enter a year:"))

if is leap year(year):
print('{}is a leap year.'. format(year))
else:
print('{} is not a leap year.'.format(year))

