# st= "my name is tisha"
# print(len(st))

# st= "MY NAME IS TISHA"
# print(str.lower(st))

# st= "my name is tisha"
# print(str.upper(st))

# st= "my name is tisha"
# print(str.capitalize(st))

# st= "my name is tisha"
# print(str.title(st))

# st= "  my name is tisha  "
# print(st.strip())

# st= "my name is tisha"
# print(st.replace('t','r',1))

# st= "my name is tisha"
# print(st.find("tisha"))

# st= "my name is tisha"
# print(st.startswith("M"))

# st= "my name is tisha"
# print(st.endswith("a"))

# st= "my name is tisha"
# print(st.split(" ",1))

# print("ABC".join("xyz"))

# print("ABC".isalpha())

# print("11111".isdigit())

# print("Tisha11".isalnum())

# print("Tisha".zfill(50))

# print("Tisha".center(50,"*"))

#Find total charcters and numbers:-

k="hello python hello 11111 ddss 22225"

# a=0
# b=0
# for i in k:
#     if str(i).isalpha():
#         a+=1
#     elif str(i).isdigit():
#         b+=1
# print("alphabet:",a)
# print("number:",b)


#Reverse string

s=""
for i in range(len(k)-1,-1,-1):
    s+=k[i]

print(s)

# print(k[5:])
# print(k[:5])
# print(k[5:9])
# print(k[-8:-1])
# print(k[::-1])

