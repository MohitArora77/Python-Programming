class Upper:
    @staticmethod
    def upper():
        u=""
        for i in range(ord("A"),ord("Z")+1):
            u+=chr(i)
        return u


class Alphabet(Upper):
    @staticmethod
    def lower():
         l=""
         for i in range(ord("a"),ord("z")+1):
             l+=chr(i)
         return l

class Numbers:
    @staticmethod
    def numbers():
        n=""
        for i in range(10):
            n+=str(i)          
        return n
class Characters(Alphabet,Numbers):
    @staticmethod
    def characters():
        s=""
        for i in range(33,127):
            if not(chr(i).isalnum()):
                s+=chr(i)
        return s

obj1=Characters()
print(obj1.characters())
print(obj1.numbers())

print(obj1.lower())
print(obj1.upper())

 