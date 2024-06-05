# //write a recursive program to print the digits  in a reverse order

def numb(num):
    if num//10==0:
        print(num)
        
    else:
        rem=num%10
        print(rem)
        numb(num//10)
        
num=int(input("enter the number"))
numb(num)

def numb1(num):
    if num<10:
        print(num)
        
    else:
        rem=num%10
        print(rem)
        numb1(num//10)
        
num=int(input("enter the number"))
numb1(num)

def numb2(num):
    if num==0:
        return
    print(num%10)
    return numb2(num//10)
num=int(input("enter the number"))
numb2(num)

