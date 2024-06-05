# //list[12,42,23,96,7,18,10,133]

list=[12,42,23,96,7,18,10,133]
min=list[0]
max=list[0]
for i in range(len(list)):
    if min>list[i]:
        min=list[i]
        minid=i
    if max<list[i]:
        max=list[i]
        maxid=i
sum=min+max
diff=max-min
list[maxid]=sum
list[minid]=diff
print(list)

