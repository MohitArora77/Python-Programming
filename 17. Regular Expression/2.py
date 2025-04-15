import re
vehicle_no="FT14BS4003 UP14YT9806 UP34re3233 74TE34ER2222"
date="25-02-2024 56-34-2344 31-02-2022 44-32-3456 20-12-2025 20-32-2024 20-12-20222"
time="15:01:32 16:40:30 234:34:234 71:23:24 24:71:29 24:43:70 60:60:60 "
gmail="abc@gmail.com wwewe123@gmail.com @gmailcomwqe1"

vehicle_no=re.findall("[A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9]{4}",vehicle_no)
print(vehicle_no)

# date=re.findall("[0-3][0-9]-[0-9]{2}-[0-9]{2,4}",date)
# print(date)

time=re.findall("[0-5][0-9]:[0-5][0-9]:[0-5][0-9]",time)
print(time)

gmail=re.findall("[A-Za-z0-9]{3}@[A-Za-z]{5}.[a-zA-Z]{3}",gmail)
print(gmail)

date1=re.findall('\d{2}-\d{2}-\d{2,4}',date)
print(date1)

data='This is Python skye eye hello ghi hell sdn first for hellww'
data1=re.findall('[A-Za-z]{3}',data)
print(data1)

data2=re.findall('\s[A-Za-z]{3}\s',data)
print(data2)

data2='pyhton123@gmail.com java@yahoo.in sql@.org'
data3='pyhton123@gmail^com java@yahoo.in sql@.org'
var=re.findall('\w*@\w*.[a-z]{2,3}',data2)
var1=re.findall('\w*@\w*\.[a-z]{2,3}',data3)
print(var)
print(var1)