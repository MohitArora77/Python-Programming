#  Write
var=open(r'C:\Users\maror\OneDrive\Desktop\P1.txt','w')
data1='Good Afternoon\n'
data2='How are you\n'
data3='What are u doing\n'
data4="Hello\n"

print(var.writelines([data1,data2,data3]))
var.close()
