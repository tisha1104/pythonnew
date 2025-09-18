from functools import reduce

# l=[16,202,250,369,14,58,30,58,20,147,11]

# def min(a,b):
#     if a<b:
#         return a
#     else:
#         return b
    
# k=reduce(min,l)
# k=reduce(lambda a,b: a if a<b else b,l)
# print(k)
    
# l=[10,20,30,40,50,60,70,80,90,100]
# def avg(numbers):
#     b=sum(numbers)/len(numbers)
#     print(b)

# # avg(l)
# # k=reduce(avg,l)
# k=reduce(lambda l: sum(l)/len(l))
# print(k)

import math

l=[1,2,3,4,5,6,7,8,9,25,49]
def check_p_square(a):
    if math.sqrt(a).is_integer():
        return a
  
# k=filter (check_p_square,l)
k=filter(lambda a:math.sqrt(a).is_integer(),l)
print(list(k))