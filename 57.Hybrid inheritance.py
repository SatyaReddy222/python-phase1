class Placements:
    def info(self):
        print("We have 623 selects still counting........!")
        print()
class Department(Placements):
    def display(self):
        print("We provide these courses:")
        print("Computer Science and Engineering")
        print("Information Technology")
        print("Mechanical Engineering")
        print("Civil Engineering")
        print("Electrical and Electronics Engieering")
        print("Electrical and Communication Engieering")
        print("Data Science")
        print("Machine Learning")
        print()
class Pragati(Department,Placements):
    def welcome(self):
        print("welcome to pragati engineering college we are glad to have you on board")
        print()
obj=Pragati()
obj.welcome()
obj.info()
obj.display()
    
        