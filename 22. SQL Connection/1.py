import sqlite3 # need to usse the proper code editor

var= sqlite3.connect('student.db') # Connect with the database

#cursor   #refrence for the execute() and commit()
a=var.cursor()

# We need to write the SQL Queries in execute using string
# a.execute("create table student('sname','rollno','addr')")

# To enter data inside the database
a.execute("insert into student values('Simon','11','Delhi')") 
a.execute("insert into student values('ABC','12','Noida')") 
a.execute("insert into student values('XYZ','13','Indrapuram')") 

# To execute the data from the table
data=a.execute("select * from student")


# print(list(data))
# print(list(data2))
print(data.fetchall())
# Reference used will be of connect function for commit and close

var.commit()
var.close()