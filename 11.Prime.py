# find whether the given number is prime or  not
import math
num=int(input("enter the number:"))
is_prime=num>1
for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            is_prime=False
            break
if(is_prime==True):
    print("given number is  a prime")
else:
    print("given number is not a prime ")
            

num=int(input("enter the number:"))
is_prime=num>1
for i in range(2,int(num/2)):
        if(num%i==0):
            is_prime=False
            break
if(is_prime==True):
    print("given number is  a prime")
else:
    print("given number is not a prime ")

