# //create a class of name placements which has a function info which displays "we have 623 selects still continuing 
# create another class named department with function display which will display the names of the departments in the college
# create a class pragati with the function welcome which displays the message welcome to pragati engineering college we are glad to have you on board.pragati class should also display the detils about departments and placements
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
class Pragati(Department):
    def welcome(self):
        print("welcome to pragati engineering college we are glad to have you on board")
        print()
obj=Pragati()
obj.welcome()
obj.info()
obj.display()

    
        