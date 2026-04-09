# Function to check Prime Number
# def Check_prime_number(n):
#         if n<=1 :
#             print("Not Prime")
#             return
#         for i in range(2,n):
#             if n%i == 0:
#                 print("Not prime number")
#                 return
            
#         print("Prime number")

# Check_prime_number(10)

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


num = 10
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

