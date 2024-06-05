# simple checking whether the given year is leap year or not
# i.if the year is divisble by 4 and not divisble 100 or if it is divisble by 400 then it is called a leap year
year=int(input("enter the year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The given year is Leap Year")
else:
    print("The given year is not a Leap Year")

