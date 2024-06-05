# //write a program to check the type of traingle where you take the input from the user for 3 sides and classify it acordingly into equlateral ,isoceles and scalane

a=int(input("enter the first side:"))
b=int(input("enter the second side:"))
c=int(input("enter the third side:"))
if(a==b==c):
    print("It's an equilateral")
elif(a==b or b==c):
    print("It's an isoceles")
else:
    print("It's an scalane")

