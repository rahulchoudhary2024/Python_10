for i in range(1,10):
    print(str(i)*i)
print()


for i in range(1,10):
     a=1
     for j in range(1,i):
         print(a,end="")
         a=a+1
     print()          
print()


j=1
for i in range(65,73):
    print(""+chr(65+j))
    j=j+1
