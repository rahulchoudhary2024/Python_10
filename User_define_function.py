#Function with no Argument & No Return Value.

def printline():
    print("*"*50)

printline()
print("welcome to user defined function in python.")
printline()


#function with argument but no return value.
def add(a,b):
    print("addition:",a+b)

printline()
add(10,20)
printline()


#function with argument & return value.

def sub(a,b):
    return a-b
printline()
#ans=sub(10,20)
print("subtraction:",sub(10,20))
printline()
