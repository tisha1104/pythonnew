char='A'
for i in range(5):
    for j in range(i+1):
        print(char,end=" ")
        char=chr(ord(char)+1)
    print()