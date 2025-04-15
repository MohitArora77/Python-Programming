Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

a=10
id(a)
140715632682184
type(a)
<class 'int'>
a=-10
id(a)
2851904052368
type(a)
<class 'int'>
a=0
id(a)
140715632681864
type(a)
<class 'int'>
>>> id(a)
140715632681864
>>> a=10
>>> b=10
>>> type(b)
<class 'int'>
>>> id(b)
140715632682184
>>> id(a)
140715632682184
>>> 
>>> a=12.0
>>> type(a)
<class 'float'>
>>> a=10.00
>>> type(a)
<class 'float'>
>>> id(a)
2851898554224
>>> a=10
>>> id(a)
140715632682184
>>> a=3++4j
>>> a=3+4j
>>> type(a)
<class 'complex'>
>>> a=3+5i
SyntaxError: invalid decimal literal
>>> a=3++4j
>>> type(a)
<class 'complex'>
>>> b=3++4j
>>> type(b)
<class 'complex'>
>>> a=True
>>> print(a)
True
>>> bool(a)
True
>>> type(a)
<class 'bool'>
