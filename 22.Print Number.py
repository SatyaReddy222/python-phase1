# //I/P=12345
# output:
#     5
#     4
#     3
#     2
#     1

num=int(input("enter the number:"))
while(num>0):
    rem=num%10
    num=num//10
    print(rem)

