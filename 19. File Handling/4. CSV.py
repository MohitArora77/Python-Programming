# Write in CSV
# import csv
# var=open('P1.txt','w')
# a=csv.writer(var)
# # print(a.writerow(['Hello','Kanishq','Gandu']))
# a.writerows([['Hello Kanishq Gandu', 'From Noida', 'Your salary is :', 456],['Hello','Mohit',567],['Hello','Rawat',578]])
# var.close()

# Read in CSV
# import csv
# var=open('P1.txt','r')
# a=csv.reader(var)
# # print(a) -> will show the Address
# print([i for i in list(a)[:] if i!=[]])
# var.close()

#  Create a file to store the data of students by using oop and file handling.
# import csv
# var=open("Student_Data.txt",'w')
# a=csv.writer(var)
# a.writerows([['std_name','rollno','phno','loc']])

# class School:
#     def __init__(self,name,rollno,phno,loc):
#         self.name=name
#         self.rollno=rollno
#         self.phno=phno
#         self.loc=loc
#         a.writerow([self.name,self.rollno,self.phno,self.loc])
# s1=School('ABC',45,9878767656,'Delhi')
# s2=School('FGH',46,9878675443,'Noida')
# s3=School('ABC',45,9786576434,'Indrapuram')
# var.close()

