#  Hybrid Inheritance -> It is the combination of 2 or more than 2 different type of inheritance.
class Upper:
    @staticmethod
    def upper():
        c1=""
        for i in range(ord('A'),ord('Z')+1):
            c1+=chr(i)
        return c1

class Alphabets(Upper):
    @staticmethod
    def lower():
        c1=""
        for i in range(ord('a'),ord('z')+1):
            c1+=chr(i)
        return c1
class Numbers:
    @staticmethod
    def numbers():
        num=''
        for i in range(0,10):
           num+=str(i)
        return num

class Characters(Alphabets,Numbers):
    @staticmethod
    def sp_chr():
        sp=""
        for i in range(32,127):
            if not ( chr(i).isalnum()):
                sp+=chr(i)
        return sp
        
print(Characters.upper())
print(Characters.lower())
print(Characters.numbers())
print(Characters.sp_chr())