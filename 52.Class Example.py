# //Create a class F15 with functions lights ,fans and AC ,display
# //lights-when light function is called it prints out the color of the light, which is taken as parameter to the funtion
# //fan-when fan function is called it displays the regulator speed in which its rotating which taken as the parameter to the function
# //AC-AC displays the room temperature and the outside temperature which are taken as parameters
# //display which displays the difference in the outside temperature and room temperature of ac and also it displays the fan speed 

class f15:
    def light(self,color):
        print("The color of me is",color)
        print("")
    def fan(self,speed):
        self.c=speed
        print("The regulator speed of the fan is",speed)
        print("")
    def ac(self,r_temp,o_temp):
        self.a=r_temp
        self.b=o_temp
        print("The room temperature is",r_temp)
        print("The outside temperature is",o_temp)
        print("")
    def display(self):
        diff=self.b-self.a
        print("The difference between outside temperature and room temperature is" ,diff)
        print("The regulator speed of the fan is",self.c)
obj=f15()
obj.light("red")
obj.fan(2)
obj.ac(16,32)
obj.display()
    

