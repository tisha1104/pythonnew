class InvalidstringException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def check(str):
    if str.isalpha():
        print("valid")
    else:
        raise InvalidstringException("sorry! Invaliid String")
    
try:
    check("ahugfygs111")
except Exception as e:
    print(e)