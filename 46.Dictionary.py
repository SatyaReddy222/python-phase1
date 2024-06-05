# create an dict with 4 value ,access your values using keys ,accessing the whole dict using for loop,try to add duplicate values,try to add duplicate keys,try to change value(mutability) remove

dict={1:"hello",2:"hi",3:"World",4:"Moshi Mosh"}
print(dict)

dict={1:"hello",2:"hi",3:"World",4:"Moshi Mosh"}
print(dict[2])

for i in dict:
    print(i,":",dict[i])

dic={1:"hello",2:"hi",3:"World",4:"Moshi Mosh" ,5:"Moshi Mosh"}
for i in dic:
    print(i,":",dic[i])

di={1:"hello",2:"hi",3:"World",4:"Moshi Mosh" ,4:"h"}
for i in di:
    print(i,":",di[i])

d={1:"hello",2:"hi",3:"World",4:"Moshi Mosh" ,4:"h"}
del d[4]
print(d)

