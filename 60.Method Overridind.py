class OverRidding:
    def bike(self):
        print("Harley Davidson")
    def laptop(self):
        print("2gb laptop with 500 HDD")
class Rid(OverRidding):
    def laptop(self):
        print("8gb ram with 500 SDD")
obj=Rid()
obj.bike()
obj.laptop()

