# def beforetest(demo):
#     def wrapper():
#         print("Call Befor Test......")
#         demo()
    # return wrapper

# @beforetest
# def test():
#     print("Test calling.......")

# @beforetest
# def demo():
#     print("Demo Calling")

# test()
# demo()


def add(calc):
    def wrapper(*a):
        print(a[0]+a[1])
        calc(*a)
    return wrapper

def mul(calc):
    def wrapper(*a):
        print(a[0]*a[1])
        calc(*a)
    return wrapper

def divi(calc):
    def wrapper(*a):
        print(a[0]/a[1])
        calc(*a)
    return wrapper

def subtrction(calc):
    def wrapper(*a):
        print(a[0]-a[1])
        calc(*a)
    return wrapper
    
@add
@mul
@subtrction
@divi
def calc(a,b):
    print("Calc operation")

calc(11,11)


def Only_number(myfun):
    def wrapper (*a):
        if not str(a[0]).isdigit():
            print("Only number is allowed")
        else:
            myfun(*a)
    return wrapper

@Only_number
def myfun(a):
    print(a)

myfun("11")

def Only_alpha(myfun):
    def wrapper (*a):
        if str(a[0]).isdigit():
            print("Only alphabet is allowed")
        else:
            myfun(*a)
    return wrapper

@Only_alpha
def myfun(a):
    print(a)

myfun("Rani")


def both(myfun):
    def wrapper (*a):
        if not str(a[0]).isalnum():
            print("does not allowed special character")
        else:
            myfun(*a)
    return wrapper

@both
def myfun(a):
    print(a)

myfun("11_tisha")


def both(myfun):
    def wrapper (*a):
        if  str(a[0]).isalnum():
            print("only special character")
        else:
            myfun(*a)
    return wrapper

@both
def myfun(a):
    print(a)

myfun("__")