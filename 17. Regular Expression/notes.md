# Regular Expression :
> Regular Expression is a process where we can use patterns to filter out or manipulate data in the string.
> AKA Regex
> To use Regex we 1st import re
> SYNTAX :
import re
data="A paragraph always starts on a new line, and is usually a block of text. The HTML
element defines a paragraph. A paragraph always starts on a new line, and browsers automatically add some white space (a margin) before and after a paragraph. You cannot be sure how HTML will be displayed."
patterns = re.findall("pattern",data)
print(patterns)

# function :
1) re.search("patterns",collection)
2) re.findall("patterns",collection)
3) re.finditer("patterns",collection)

# Patterns :
> [A-Z] -> To match the one uppercase character
> [a-z] -> To match the one lowercase character
> [0-9] -> To match the one digit character
> [A-Za-z0-9] -> To match the one uppercase , one lowercase , one digit character.
> [A-Z]{m,n} -> To match the characters b/w  m to n
> [A-Z]{n} -> to match n no. of characters
> \d -> to match one digit
> \b -> to match the spcae around the string
> \s -> to match one single space
> \w -> to match one alphanumeric 
> \W -> to match one non-alphanumeric 
>  + -> to match 1 to n characters
>  * -> to match 0 to n characters
>  ? -> to match 0 or 1 characters

# Meta Characters :
Character	Description	                                                               Example	
[]	        A set of characters	                                                       "[a-m]"	
\	        Signals a special sequence (can also be used to escape special characters)	"\d"	
.	        Any character (except newline character)	                               "he..o"	
^	        Starts with	                                                               "^hello"	
$	        Ends with	                                                               "planet$"	
*	        Zero or more occurrences	                                               "he.*o"	
+	        One or more occurrences	                                                   "he.+o"	
?	        Zero or one occurrence	                                                   "he.?o"	
{}	        Exactly the specified number of occurrences	                               "he.{2}o"	
|	        Either or	                                                               "falls|stays"	
()	        Capture and group