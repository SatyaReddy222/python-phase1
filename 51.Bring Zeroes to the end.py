# //list[2,0,1024,0,40,230,0]

List = [2, 0, 1024, 0, 40, 230, 0]
index = 0

for i in range(len(List)):
    if List[i] != 0:
        List[index] = List[i]
        index += 1

while index < len(List):
    List[index] = 0
    index += 1

print("List:",List)

List = [2, 0, 1024, 0, 40, 230, 0]
l2=[]
for i in range(len(List)):
    if List[i] != 0:
        l2.append(list[i])
for i in range(len(list)):
    if List[i] == 0:
        l2.append(list[i])
print(l2)

