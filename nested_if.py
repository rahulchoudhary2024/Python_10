a=int(input("enter value for A :"))
b=int(input("enter value for B :"))
c=int(input("enter value for C :"))

if a>b:
    if a>c:
        print("a is max")
    else:
        print("c is max")

elif b>c:
    print("b is max")
else:
    print("c is max")
