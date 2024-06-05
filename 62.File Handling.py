import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["student Id","Name","Phone Number"])
studentId=int(input("enter the student ID:"))
Name=input("enter the student name:")
ph_no=int(input("enter the student phone number:"))
a.writerow([studentId,Name,ph_no])
print("student record has save")