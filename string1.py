s=input("Enter String : ")

al=0
nm=0
sp=0
uc=0
lc=0
sc=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1
    elif not i.isalnum(): 
        sc=sc+1
        
print("Total Alphabets : ",al)
print("Total Numeric : ",nm)
print("Total Space : ",sp)
print("Total Upper Case : ",uc)
print("Total Lower Case : ",lc)
print("special charecter",sc)
