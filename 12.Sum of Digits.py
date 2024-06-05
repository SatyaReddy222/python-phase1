# //Calculate the sum of the digits of a number which is taken as input from the user

num=int(input("enter the number:"))
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
print("The sum of the digits:",sum)
    

