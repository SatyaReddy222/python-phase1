# //take a number input from the user check if the sum of factors of its numbers is greater than the orginal number or not if yes print yes else no

num=int(input("enter the number:"))
sum=0
for i in range(1,int(num/2+1)):
    if(num%i==0):
        sum=sum+i
if(sum>=num):
    print("yes")
else:
    print("no")

num=int(input("enter the number:"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum>=num):
    print("yes")
else:
    print("no")

