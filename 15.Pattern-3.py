# *****
# ****
# ***
# **
# *
# find the pattern

for i in range(1,6):
    for i in range(1,6-i+1):
        print("*",end="")
    print()
    
#second way
for i in range(5,0,-1):
    for i in range(1,i+1):
        print("*",end="")
    print()

