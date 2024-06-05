# //create a class ticket which will be the abstract class inside that create a function book ticket which will be the abstract method and has nothing in it.Create a class make_my_trip which will use the book ticket function from ticket class to take the details such as name,phonenumber,email id,journey,date and displays the message saying thank you for booking from make_my_trip.create a class irctc which uses the book ticket of ticket class and takes the same details as make_my_trip but in the end it will give an option to user to select whether it is one way or round trip if the user option is round trip it again asks the user to enter the return date as well and then prints the message thank you for choosing irctc else it prints thank you for choosing irctc.create a class indigo  which takes all the details as irctc and just asks which mode of transport you want to go in train flight or bus and displays thank you choosing indigo

from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def book_ticket(self, name, ph_no, email, journey_date):
        pass

class MakeMyTrip(Ticket):
    def book_ticket(self, name, ph_no, email, journey_date):
        print("Thanks for booking from Make My Trip")

class IRCTC(Ticket):
    def book_ticket(self, name, ph_no, email, journey_date):
        trip = input("Enter the journey whether round or one-way: ")
        if trip.lower() == "round":
            end = input("Enter the return date: ")
        print("Thanks for booking from IRCTC")

class Indigo(Ticket):
    def _init_(self,name,ph_no,email,journey_date):
        mode = input("Enter which mode you want to travel (train, bus, flight): ")
        print("Thanks for Choosing Indigo")
name = input("Enter your name: ")
ph_no = input("Enter your phone number: ")
email = input("Enter your email: ")
journey_date = input("Enter the journey date: ")

n=int(input("enter the 1 for Make My Trip 2 for IRCTC 3 for Indigo"))
match n:
    case 1:
        obj1 = MakeMyTrip()
        obj1.book_ticket(name, ph_no, email,journey_date)
    case 2:
        obj2=IRCTC()
        obj2.book_ticket(name, ph_no, email,journey_date)
    case 3:
        obj3=Indigo()
        #obj3.book_ticket(name, ph_no, email,journey_date)
    case _:
        print("enter the valid option")

