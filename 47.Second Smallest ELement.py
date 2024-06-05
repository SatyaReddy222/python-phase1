# //l=[22,-1,42,65,1,-4,6] write a program to find the second smallest number negative number form this wihtiout using max and min

l = [22,-1, 42, 65, 1, -4, 6]
minv = l[0]
second = 0

for i in range(1, len(l)):
    if l[i] < minv:
        minv = l[i]

for i in range(len(l)):
    if l[i] != minv:
        if second == 0 or l[i] < second:
            second = l[i]

print("Second smallest value:", second)

list=[22,-1,42,65,1,-4,6]
m1=999
m2=999
for i in range(len(list)):
    if list[i]<m1:
        m2=m1
        m1=list[i]
print("Second Smallest Value:",m2)


list=[22,-1,42,65,1,-4,6]
m1=0
m2=0

for i in range(len(list)):
    if list[i]>m1:
        m2=m1
        m1=list[i]
print("Second Smallest number:",m2)


def func():
    nums=[22,-1,42,65,1,-4,6]
    min=nums[0]
    min1=nums[0]
    min2=nums[0]
    for i in range(len(nums)):
        if nums[i]>min:
            min=nums[i]
    for i in range(len(nums)):
        if nums[i]>min1 and nums[i]!=min:
            min1=nums[i]
    for i in range(len(nums)):
        if nums[i]>min2 and nums[i]!=min and nums[i]!=min1: #3rd smallest
            min2=nums[i]
    print(min2)
func()

