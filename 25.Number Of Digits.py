# //I/P 1 2 3 4 5
# O/P 5

num=int(input("enter the number:"))
count=0
while(num>0):
    rem=num%10
    num=num//10
    count=count+1
print(count)

