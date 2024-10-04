name="hello"
name.capitalize()
print(name)
formatt = "{:2f}".format(3.14159)
print(formatt)
dict = {"name" : "arnav", "age" : 19}
dict.get("name")
for i in range(6) :
    if i==4 :
        continue
    elif i==5 :
        break
    print(i)