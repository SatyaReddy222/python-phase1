class f15:
    def __init__(suresh,s_time,e_time):
        suresh.s_time=s_time
        suresh.e_time=e_time
        print("The placement for this year is 657")
        #print("The mul of a and b:",a*b)
        print()
    def light(suresh,color):
        print("The color of me is",color)
        print()
    def fan(suresh,speed):
        suresh.c=speed
        print("The regulator speed of the fan is",speed)
        print()
    def ac(suresh,r_temp,o_temp):
        suresh.a=r_temp
        suresh.b=o_temp
        print("The room temperature is",r_temp)
        print("The outside temperature is",o_temp)
        print()
    def display(suresh):
        diff=suresh.b-suresh.a
        print("The difference between outside temperature and room temperature is" ,diff)
        print("The regulator speed of the fan is",suresh.c)
        print("The class starts at:",suresh.s_time)
        print("The class ends at:",suresh.e_time)
        
obj=f15("9:00AM","4:00PM")
obj.light("red")
obj.fan(2)
obj.ac(16,32)
obj.display()
    

