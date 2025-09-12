lines=5
for i in range(lines):
    for k in range(lines-i):
        print(" ",end="")
    for j in range(i+1):
        if j==0 or j==(i):
         print("* ",end="")
        else:
         print("  ",end="")
    print()
for i in range(lines-1,0,-1):
   for k in range((lines-1)-i+2):
      print(" ",end="")
   for j in range(i):
        if j==0 or j==(i-1):
            print("* ",end="")
        else:
            print("  ",end="")
   print()