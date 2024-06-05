# //caluclate the difference of sum of numbers that are divisble by 6 not divisble by 6 in the range of first 30 numbers

divby=0
notdivby=0
for i in range(1,31):
    if(i%6==0):
        divby=divby+i
    else:
        notdivby=notdivby+i
diff=notdivby-divby
print(diff)

