# //Write a function to design a basic login function and make sure to print successful login if username and password is same

def loginPage():
    while True:
        username=input("enter the username:")
        password=input("enter the password:")
        if(username==password):
            print("login successful")
            break
        else:
            print("enter the correct credentials")
        
            
loginPage()

