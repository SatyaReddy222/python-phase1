num=int(input("enter the number:"))
original=num
reverse=0
while(num>0):
    rem=num%10
    reverse=reverse*10+rem;
    num//=10;
if(original==reverse):
    print("The given number is palindrome")
else:
    print("The given number not a palindrome")

