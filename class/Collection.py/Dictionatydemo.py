st ={ 
    "Name":"Tisha",
    "email":"tishapatel@gmail.com",
    "lang":["Guj","Hindi","Eng"]
}

print(st)
print(st["Name"])
print(st.get("Name"))

st["Name"]="Rani"
print(st["Name"])
st["Contact"]="12365687"
st.update({"Subject":"Python","stram":"IT"})
print(st["lang"][0])
print(st)


a= dict(Name="Rani",email="Rani@gmail.com")
print(a)
print(a["Name"])
print(a.get("Name"))
print(a.keys())
print(a.values())
print(a.items())


for i,j in a.items():
    print(i,j)


a["Name1"]="Tisha"
a.update({"Name":"Tisha","Phone":"88562310"})
a.pop("Name")
a.popitem()
a.clear()
print(a)

students={
    "Rani":{
        "email":"Rani@gmail.com",
        "Phone":"88666068756"
    },
    "Tisha":{
        "email":"Tisha@gmail.com",
        "Phone":"4569895320368"
    }
}

for i,j in students.items():
    print(i)
    for a,b in j.items():
        print(a,b)


x= ('Keys1','Keys2','Keys3')
y= "Hello"

t=dict.fromkeys(x,y)
print(t)

l=[1,2,3,4,5]
a="Rani"

k=dict.fromkeys(l,a)
print(k)