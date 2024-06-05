def SumofDig(num):
    if num == 0:
        return 0
    
    rem = num % 10
    return rem + SumofDig(num // 10)

num = int(input("Enter the number: "))
result = SumofDig(num)
print("Sum of digits:", result)


