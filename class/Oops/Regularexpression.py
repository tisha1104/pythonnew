import re

# k=re.match('H.l',"aHello python")
# k=re.search('H.l',"aHello python")
# k=re.findall('H.l',"aHello python")

# k=re.match('^Hello',"Hello pytHoln")
# k=re.search('abc$',"Hello pytHoln abc")
# print(k)

k = re.findall('[0-9]',"Hello pyt 1 Ho 3ln abc")


k = re.findall('\W',"Hello pyt @ 1 Ho 3ln abc")

k = re.findall('la{2}l',"Helaaalo pyt @ 1 Ho 3ln abc")
print(k)

num = input("Enter your number: ")
k = re.match('[0-9]{10}$',num)
if k:
    print("Valid number")
else:
    print("Invalid number")

#tops@gmial.com
email = input("Enter your email: ")
k = re.match('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email)
if k:
    print("Valid email")    
else:
    print("Invalid email")