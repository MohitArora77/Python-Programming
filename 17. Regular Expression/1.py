#Regular Expression : It is the process of writing a pattern to filter the data from a huge data that is nothing but string.
# RE-Module (re stands for Regular).
# .findall -> fetch all the data.
#  syntax:-->
# import re
# var= re.findall('pattern',data/var)

import re
data="Hello Kanishq 37946827 372623874 9878767656 8768767654 DFLYS7584T YTEET1234T ERZTW4567Y"
var=re.findall("[6-9][0-9]{9}",data)
var1=re.findall("[A-Z][a-z]{9}",data)
var2=re.findall("[A-Z]{5}[0-9]{4}[A-Z]",data)
print(var)
print(var1)
print(var2)

