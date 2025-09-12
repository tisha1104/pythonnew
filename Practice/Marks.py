choice="y"
while choice != "n" :
    marks=int(input("Enter the Marks"))

    if marks>=91 and marks<=100:
        print("your grade is A")
    elif marks>=71 and marks<=90:
        print("your grade is B")
    elif marks>=51 and marks<=70:
        print("your grade is C")
    elif marks>=35 and marks<=50:
        print("your grade is D")
    else:
        print("invalid input if out of range(0-100)")

    choice=input("do you want to continue? yes or no ")