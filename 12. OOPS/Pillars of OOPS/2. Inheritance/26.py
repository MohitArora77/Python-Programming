# multilevel inheRitance
class Add:
   @staticmethod
   def add(a,b):
     return a+b
class Mul:
   @staticmethod
   def mul(a,b):
      return a*b
class Sub:
    @staticmethod
    def sub(a,b):
        return b-a
class Calculator(Add,Mul,Sub):
    @staticmethod
    def div(a,b):
        return a/b
obj1=Calculator()
print(obj1.add(2,3))
print(obj1.mul(2,3))
print(obj1.sub(2,3))
print(obj1.div(2,3))