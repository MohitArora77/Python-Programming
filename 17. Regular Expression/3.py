# Regular Expression (Regex) :

import re
patterns=r"[A-Z]ine"
data="A paragraph always starts on a new line, and is usually a block of text. The HTML element defines a paragraph. A paragraph always starts on a new Fine, and browsers automatically add some white space (a margin) before and after a paragraph. You cannot be sure how HTML will be displayed."
# patterns = re.findall("[a-z]{7}",data)

# Search function ->
# match=re.search(patterns,data)
# print(match)

# Meta characters -> 

# var=re.findall("[A-Z][a-z]{3}",data)
# print(var)

# var=re.finditer(patterns,data)
# print(var)
# for i in var:
#     print(i)
    
# Regular Expression -> using meta characters

# 1. [ ] -> able to find the character 
# import re
# data="HEllo how are you? My friend"
# x=re.findall("[A-Z][A-Z][a-z]{3}",data)
# print(x) # ['HEllo']

# 2. \ --> able to find all the digit character
# import re
# data1="Hello Are you guys ok ? 58 is my house number if u wana come by and have some drinks"
# x1=re.findall("\d",data1)
# print(x1) # ['5', '8']

# 3. '.' -> for the number of character ( 1 character = 1 '.')
# import re 
# data="Hello yellow bellow teoll ready killer miller"
# x=re.findall("ye..ow",data)
# print(x) #['yellow']

# 4. ^ -> starts with
# import re
# data="hello how are you"
# data1="hell how are you"
# x=re.findall("^hello",data)
# x1=re.findall("^hello",data1)
# print(x) # ['hello']
# print(x1) # [] -> empty list bcz the data is not start with "hello"

# 5. $  -> ends with

# import re
# data="hello how are you"
# data1="hell how are you"
# x=re.findall("you$",data)
# x1=re.findall("the$",data1)
# print(x) # ['you']
# print(x1) #[]

# 6. * -> to match 0 to n no. of characters (range purpose)

# import re
# data="hello hi what are you doing today?"
# x=re.findall("he.*w",data) # need to use '.'
# print(x) #['hello hi w'] from this character "h" to the character "w" 

# 7. + -> to match 1 to n no. of characters (range purpose)
# import re
# data="hello hi what are you doing today?"
# x=re.findall("he.+o",data) # need to use '.'
# print(x) #['hello hi what are you doing to']

# 8. ? -> to match 0 or 1 characters 
# import re
# data="hello hi what are you doing today?"
# x=re.findall("d.?g",data)
# x1=re.findall("d...?g",data)
# print(x) # []
# print(x1) # ['doing']

# 9. {} 
# import re
# data="hello hi what are you doing today?"
# x=re.findall("he.{2}o",data)
# print(x)

