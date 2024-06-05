class Faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print("faculty_information:",self.f_name,self.department,self.f_id)
obj=Faculty("Sai Kiran Sir","Civil",101)
obj.print_info()
class Ce(Faculty):
    pass#no statement
obj=Ce("Sarooja mam","Civil",102)
obj.print_info()

