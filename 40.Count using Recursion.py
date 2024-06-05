# //write a recursive funtion to count the number of digits of a number

def numb(num):
    if num<10:
        return 1 
    return 1+numb(num//10)
num=int(input("enter the number:"))
numb(num)

def numb(num):
    if num==0:
        return 0 
    return 1+numb(num//10)
num=int(input("enter the number:"))
numb(num)

