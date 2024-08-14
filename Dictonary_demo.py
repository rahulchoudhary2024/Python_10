d={145:"Ajay",908:"Vijay",765:"jay",654:"Kamal",999:"Karan"}

print(d)
print(d[908])
print(d.get(765))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(908))
print(d.popitem()) 

print("***********************************************************************")

d1= {1:"vijay",2:"karan",145:"ketan"}
d.update(d1)
print(d)

for i in d:
    print(i,":",d[i])
