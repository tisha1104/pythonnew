lines=5
for i in range(1,lines+1):
    for j in range(1,lines+1):
        if i%2==0:
            print("*",end="")
        # elif j%2!=0:
        #     print("*",end="")
        else:
            print(" ",end="")
    # for i in range
    print() 
    # for i in range(1,lines+1):
    #      print("* "*i)
    # for i in range(lines-1,0,-1):
    #     print("* "*i)