#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         *

rows=5
for i in range(rows-1):
    for s in range(rows-i-1):
        print("  ",end="") 
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(4,-1,-1):
    for s in range(rows-i-1):
        print("  ",end="") 
    for j in range(2*i+1):
        print("*",end=" ")
    print()

