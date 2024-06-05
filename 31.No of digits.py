a=1578
temp=a
temp1=a
count=0
while a>0:
    count=count+1
    a=a//10
print(count)
sum=0
while temp1>0:
    temp=temp%10
    sum=sum+(temp**count)
    count=count-1
    temp1=temp1//10
print(sum)