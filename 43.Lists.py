#print list
list=[1,2,3,4,5,6,7,8,9,10]
print(list)

#slicing
list=[1,2,3,4,5,6,7,8,9,10]
print(list[1:3])
print(list[-1:])
print(list[0:3])
print(list[3:8])

#accessing
list=[1,2,3,4,5,6,7,8,9,10]
print(list[3])
print(list[8])
print(list[2])

#appending list using loops
l=[]
num=10
print("enter the elements:")
for i in range(num):
    l.append(input())
print(l)

#insert
list=[1,2,3,4,5,6,7,8,9,10]
list.insert(2,30)
print(list)

#append
list=[1,2,3,4,5,6,7,8,9,10]
list.append(20)
print(list)

#multidimensional list
list1=[[11,12,13],
      [14,15,16],
      [17,18,19]]
print(*list1,sep="\n")

#remove
list=[1,2,3,4,5,6,7,8,9,10]
list.remove(1)
print(list)

