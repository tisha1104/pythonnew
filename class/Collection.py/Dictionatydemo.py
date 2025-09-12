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