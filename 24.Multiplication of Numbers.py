# I/P:12345
# O/P:120

num=int(input("enter the number:"))
mul=1
while(num>0):
    rem=num%10
    num=num//10
    mul=mul*rem
print(mul)

