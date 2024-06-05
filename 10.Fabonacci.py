# print first 10 fabinaaci series

first=0
second=1
temp=0
print(first)
for i in range(2,11):
    first=second
    second=temp
    temp=first+second
    print(temp)

first=0
second=1
temp=0
print(first)
print(second)

for i in range(3,11):
    temp=first+second
    print(temp)
    first=second
    second=temp
    

