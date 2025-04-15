# File Handling:
<!-- File -->
> File is a container which contains the data.
> By the help of extension one can know which type of the data is stored inside the file.

<!-- File Handling -->
> It is the process of writing the data into the file or reading the data from the file.
> To Perform File handling 1st we need the access of their file.

<!-- To Access the file -> Syntax -->
> var=open('File_name.extension/location of the file', 'mode (write or read)'  )

# Mode : 
> The types of operations we want to perform on the file.

# Types of Modes:
> There are 3 types of modes
 1) Write Mode (w)
 2) Read Mode (r)
 3) Append Mode (a)

# 1) Write Mode :
> It is denoted the 'w'.
> It is used to write the data inside of the file.
> In this case if the file exists -> It will overide the file , if doesn't exists then it will create a new file.

<!-- We have 2 function in write mode  -->
1) write(): 
> It is used to write single line of data.
> syntax : data='str' -> var.write(data)

2) writelines():
> It is used to write multiple lines of data.
> syntax: 
> data1='str1' data2='str2' data3='str3'
> var.writelines([data1,data2,data3]) // we need to create a list to store multiple data in writelines function.

3) close():
> It is used to commit/save the data inside the file.
> synatx : var.close()

# 2) Read Mode :
> denoted by 'r'.
> It used to read the data from the file.
> If file exists -> Read the data , if not exists then throw error.
> This mode is known as the default mode.

<!-- Read functions -->
1) read():
> This function is used to get the entire content of the file.
> Syntax: data=var.read()

2) readline():
> It will read one line of statement at a time
> syntax: data=var.readlines()

3) readlines():
> It will read all the lines from the file.
> It will return a list contaning all the lines as substring.
> syntax : data =var.readlines() 

# 3) Append Mode :
> Denoted by 'a'.
> In this mode it will not overide the previous data instead add the new data with the existing data.
> This is used for Update the data in the file.
> same functions as write
<!-- Syntax -->
var=open('file_name.extension/location','a')
var.write()
var.writelines()

# CSV file->
> Comma Seperated value
> It is file where data is stored with sepration of comma.
> In the real time application data stored in CSV file.
> We can store the data -> str, numbers

# How to write the data into the CSV file.
import CSV
var=open("File_name.extension/location, 'w')
a = csv.writer(var)
a.writerow()
a.writerows()
var.close()
# Functions:

1) Writerow():
> It is used to write single row at a time inside the file in the form of list.
a.writerow([data1,data2,data3....datan])

2) Writerows():
> It is used to write multiple rows at a time in the form of list.
a.writerows([data1,data2....datan],[data1,data2...datan],[data1,data2,..datan])

# How to read in the CSV file.

import csv
var=open('File_name.exe/loc','r')
a=csv.reader(var)
print(list(a))


