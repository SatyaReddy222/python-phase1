# //car company contains toyota mahindra and mercedes
# //take the input from the user for the car company name and in the input message give the user 3 options of 3 company the user input company name goes as the input/argument to model name funtion,which welcomes the user accordingly to the company name.ask the user to enter the specific model name for that company
# //the second function whose name variant according to the car company name and car model  the user should be asked to enter the variant he would likes to choose from petrol diesel 
# //the last display function according to the car company ,car model name and car varient first its ex-showroom price should be displayed and then is on-road price should be displayed ,which is calculated as ex-showroom price + cgst+sgst+insurance. the sgst ,cgst and the insurance all the there  have a common a value  throught the car showroom

class CarShowRoom:
    def __init__(self, name):
        self.name = name
        self.insurance = (5/100)
        self.cgst = (3/100)
        self.sgst = (2/100)
        if name == "toyota":
            print("Welcome to Toyota Family")
            self.model = self.carmod(name)
            self.vari = self.carvar(self.model, name)
            self.display(name, self.model, self.vari)
        elif name == "mahindra":
            print("Welcome to Mahindra Family")
            self.model = self.carmod(name)
            self.vari = self.carvar(self.model, name)
            self.display(name, self.model, self.vari)
        elif name == "mercedes":
            print("Welcome to Mercedes Family")
            self.model = self.carmod(name)
            self.vari = self.carvar(self.model, name)
            self.display(name, self.model, self.vari)
        else:
            print("No such car company is present in our showroom please select a valid car company")

    def carmod(self, name):
        if name == "toyota":
            mod = input("select one from hycross and glanza:")
            if mod == "hycross" or mod == "glanza":
                return mod
            else:
                print("select appropriate options")

        elif name == "mahindra":
            mod = input("select one from thar and xuv700:")
            if mod == "thar" or mod == "xuv700":
                return mod
            else:
                print("select appropriate options")
        elif name == "mercedes":
            mod = input("select one from cqs and gls:")
            if mod == "cqs" or mod == "gls":
                return mod
            else:
                print("select appropriate options")

    def carvar(self, model, name):
        var = input("select which variant you want (petrol,diesel):")
        if model=="hycross" and name=="toyota"and var== "petrol":
            return var
        elif model=="hycross" and name=="toyota" and var== "diesel":
            return var
        elif model=="glanza" and name=="toyota" and var== "petrol":
            return var
        elif model=="glanza" and name=="toyota" and var== "diesel":
            return var
        elif model=="thar" and name=="mahindra" and var== "petrol":
            return var
        elif model=="thar" and name=="mahindra" and var== "diesel":
            return var
        elif model=="xuv700" and name=="mahindra" and var== "petrol":
            return var
        elif model=="xuv700" and name=="mahindra" and var== "diesel":
            return var
        elif model=="cqs" and name=="mercedes" and var=="petrol":
            return var
        elif model=="cqs" and name=="mercedes" and var=="diesel":
            return var
        elif model=="gls" and name=="mercedes" and var=="petrol":
            return var
        elif model=="gls" and name=="mercedes" and var=="diesel":
            return var
        else:
            print("select appropriate options")

    def display(self, name, model, var):
        if model == "hycross" and name == "toyota" and var == "petrol":
            exshow = 2000000
            print("The ex-showroom price of Toyota's hycross model petrol variant is", exshow)
            onroad = exshow+(exshow * self.insurance) + (exshow * self.sgst) + (exshow * self.cgst)
            print("The on-road price of Toyota's hycross model petrol variant is", onroad)
        elif model=="hycross" and name=="toyota" and var== "diesel":
            exshow=1977000
            print("The ex-showroom prince of toyota's hycross model diesel varient is",exshow,)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of toyota's hycross model diesel varient is",onroad)
        elif model=="glanza" and name=="toyota" and var== "petrol":
            exshow=1854000
            print("The ex-showroom prince of toyota's glanza model petrol varient is",exshow,)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of toyota's glanza model petrol varient is",onroad)
        elif model=="glanza" and name=="toyota" and var== "diesel":
            exshow=1800000
            print("The ex-showroom prince of toyota's glanza model diesel varient is",exshow,)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of toyota's glanza model diesel varient is",onroad)
        elif model=="thar" and name=="mahindra" and var== "petrol":
            exshow=1000000
            print("The ex-showroom prince of mahindra's thar model petrol varient is",exshow,)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of mahindra's thar model petrol varient is",onroad)
        elif model=="thar" and name=="mahindra" and var== "diesel":
            exshow=981000
            print("The ex-showroom prince of mahindra's thar model diesel varient is",exshow)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of mahindra's thar model diesel varient is",onroad)
        elif model=="xuv700" and name=="mahindra" and var== "petrol":
            exshow=2000000
            print("The ex-showroom prince of mahindra's xuv700 model petrol varient is",exshow)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of mahindra's xuv700 model petrol varient is",onroad)
        elif model=="xuv700" and name=="mahindra" and var== "diesel":
            exshow=1980000
            print("The ex-showroom prince of mahindra's xuv700 model diesel varient is",exshow)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of mahindra's xuv700 model diesel varient is",onroad)
        elif model=="cqs" and name=="mercedes" and var=="petrol":
            exshow=15000000
            print("The ex-showroom prince of mercedes's cqs model petrol varient is",exshow)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of mercedes's cqs model petrol varient is",onroad)
        elif model=="cqs" and name=="mercedes" and var=="diesel":
            exshow=14000000
            print("The ex-showroom prince of mercedes's cqs model diesel varient is",exshow)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of mercedes's cqs model diesel varient is",onroad)
        elif model=="gls" and name=="mercedes" and var=="petrol":
            exshow=13000000
            print("The ex-showroom prince of mercedes's gls model petrol varient is",exshow)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of mercedes's gls model petrol varient is",onroad)
        elif model=="gls" and name=="mercedes" and var=="diesel":
            exshow=12000000
            print("The ex-showroom prince of mercedes's gls model diesel varient is",exshow)
            onroad=exshow+(exshow*self.insurance)+(exshow*self.sgst)+(exshow*self.cgst)
            print("The onroad prince of mercedes's gls model diesel varient is",onroad)


name = input("enter the car company you need select from these three (toyota, mahindra, mercedes): ")
obj = CarShowRoom(name)


