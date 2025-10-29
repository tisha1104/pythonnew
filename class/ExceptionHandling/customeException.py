class AgeinvalidException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def agechecker(age):
    if age<18:
        raise AgeinvalidException("Invalid age ")
    else:
        print("Valid age")

print("Program started")
try:
    agechecker(11)
except Exception as e:
    print(e)
print("program ended")