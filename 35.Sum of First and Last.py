# //write a function to calculate sum of first and last digit of a number

def sum(num):
    last=num%10
    while num>10:
        num=num//10
    sum=last+num
    return sum
num=int(input("enter the number"))
sum(num)


