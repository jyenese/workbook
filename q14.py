# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

# This is pseudocode

function is_prime(num)
    for x in range(2, num):
        if (num modulus x) == 0:
            return False
    return True

for i in range(1...100)
    if is_prime(i)
        print "{i} is prime"
    

# This is written in python

def is_prime(num):
    for x in range(2, num):
        if (num%x) == 0:
            return False
    return True
        
for i in range(1, 101):
    if is_prime(i):
        print("Is prime", i)


            
            
        
