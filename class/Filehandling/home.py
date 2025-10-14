f=open("test.txt",'w')
f.write("Hello Python!")
f.close

# f=open("C:\\test.txt",'w')
# f.write("Hello Python!")
# f.close

# f=open("test.txt",'a')
# f.write("\n Hello Java!")
# f.close

# f=open("test.txt",'r')
# data=f.read()
# print(data)

# f=open ("test.txt",'r')
# while True:
#      data=f.readline()
#      print(data)
#      if 'Python' in data:
#           print(data)
#      if not data:
#           break
     
# f=open ("test.txt",'r')
# while True:
#      data=f.readline()
#      print(len(data))
#      if 'java' in data:
#           print(data)
#      if not data:
#           break

# f=open("test.txt",'r')
# data=f.readlines()
# print(data)

with open('test.txt','r')as f:
    print(f.tell())
    f.seek(5)
    print(f.tell())
    data=f.read()
    print(f.tell())
    print(data)

# with open('test.txt','r+')as f:
#     f.write("something")
#     f.seek(0)
#     data=f.read()
#     print(data)

# with open("test.txt",'w+')as f:
#     f.write("something")
#     f.seek(0)
#     data=f.read()
#     print(data)

# with open("C:\Tisha\pythonnew\class\Filehandling\image.png",'rb')as f:
#     data=f.read()
#     print(data)