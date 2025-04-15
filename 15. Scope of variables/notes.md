# Scope of variables:
> Scope of variables refers to the region/space of the module where we can write(modify) and read(access) the values of the variable. 

* In Python we have LEGB rule:
1) L-> Local Scope. 
2) E-> Enclosed Scope/Non-Local Scope.
3) G-> Global Scope.
4) B-> Built-In Scope.

* note:-> In Nested function ineer will be local Scope and outer function will be Enclosed Scope.

# Built-In Scope Variable:

> The Utility function like -> print(),len(),input(),int(),type() are belongs to Built-In Scope of variable.

> We can Access these inside of the any module.

# Global Scope:

> These are the Variables which are declared at the main space of a module or outside of the Class or a Function.

> To Access these values in the main space, inside the class and inside the function.

> We can Modify the Global Sccope at Main Space only.

> If we want to modify global variable we need to use keyword called global in the function or in class , and we can modify.

# Enclosed / Non-local Scope:

> These are the variable declared inside of a enclosed function.

> The life span of that variable remains inside of that function only.

> We can access that variable inside the function only.


# Local Scope:

> if you declare any varibale inside of the function then that will be known as local scope the variable.

<!-- Built-In> Global > Enclosed > Local -->