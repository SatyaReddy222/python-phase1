# //take an integer as an input from the user and check whether if the number is divisble by sum of digits or not

num=int(input("enter the number:"))
num1=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
print("The sum of the digits:",sum)
if(num1%sum==0):
    print("The given number is divisble by its sum of its digit")
else:
    print("The given number is not divisble by its sum of its digit")

