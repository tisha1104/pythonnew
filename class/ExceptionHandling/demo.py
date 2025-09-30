# print("Program Started")
# try:
#     a=10
#     b=a/0
#     print(b)
# except Exception as c:
#     print(c)
# print("Program ended")

# print("Program Started")
# try:
#     a=10
#     b=a/0
#     print(b)
# except Exception as c:
#     print(c)
# else:
#     print("everything is oky")
# finally:
#     print("Always executable")
# print("Program ended")

# f=""
# try:
#     f=open("test.txt","r")
#     data=f.read()
#     print(data)
# except Exception as a:
#     print(a)
# finally:
#     if(f is not None):
#         f.close()

def test():
    try:
        a=int(input("Enter number:"))
        return 1
    except Exception as c:
        return 0
    finally:
        print("Program exected...")

a=test()
print(a)