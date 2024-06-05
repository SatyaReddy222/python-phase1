def fiorder(num, order=0):
    if num > 0:
        return fiorder(num // 10, order + 1)
    return order

def armstrong(num, original, order):
    if num > 0:
        rem = num % 10
        return armstrong(num // 10, original, order) + rem ** order
    return 0

num = int(input("Enter the number: "))
original = num
order = fiorder(num)
arm = armstrong(num, original, order)

if original == arm:
    print("The given number is Armstrong.")
else:
    print("The given number is not an Armstrong.")


