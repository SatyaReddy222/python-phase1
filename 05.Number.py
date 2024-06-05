# write a program in which you take an integer input from the user
# i.if the integer is divisble by 3 and 6 then print good number
# ii.if the integer is divisble 2 and 7 then print average number
# iii.if the integer is divisible by 4 or 9 then print awesome number
# iv.else print bad number

num=int(input("enter the number:"))
if (num%3==0 and num%6==0):
    print("Good Number")
elif (num%2==0 and num%7==0) :
    print("Average Number")
elif (num%4==0 or num%9==0):
    print("Awesome Number")
else:
    print("Bad Number")