'''
Type Of If

1. Simple If

    if condition:
        statement

2. if/else

    if condition:
        statement
    else:
        statement

3. Nested if

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement

4. Ladder if

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
'''
a=int(input("Enter Value Of A : "))
b=int(input("Enter Value Of B : "))
if a>b:
    print("A Is Max Value")
else:
    print("B Is Max Value")
