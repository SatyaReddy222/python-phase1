#     *    
#    * *   
#   *   *  
#  *     * 
# *********
rows = 5

for i in range(1, rows + 1):
    for j in range(1, (rows * 2)):
        if i == rows or i + j == rows + 1 or j - i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
       