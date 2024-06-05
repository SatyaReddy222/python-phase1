# //armstrong number

num=int(input("enter the number:"))
original=num
arm=0
order=0
temp=original
while temp > 0:
    temp//= 10
    order += 1
while num>0:
    rem=num%10
    num//=10
    arm=arm+rem**order
if original==arm:
    print("the given number is arm strong")
else:
    print("the given number is not an arm strong")

