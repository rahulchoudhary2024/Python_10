file=open("tops2.txt","w")
file.write ("this is file management demo using python.")
file.close()
print("file written successfully")
print("*****************************")
file = open("tops2.txt","r")
print(file.read())
file.close()
print("*****************************")
file=open("tops2.txt","a")
file.write("\n this file is now appended")
file.close()
print("*****************************")
file= open("tops2.txt","r")
print(file.read())
file.close()
print("*****************************")

file=open("tops3.txt","w+")
file.write("this is W+ mode using python.")
print("current file position :",file.read())
file.seek(0)
print("file data :",file.read())
file.close()
