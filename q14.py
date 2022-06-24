# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
# number = 0
# number = 1

# need to ask if its dividable by 2
# if yes, print is a prime 
# if no, print isnt a prime



prompt = print("Is it a prim number?")
def _prime_number(index):
    num1 = index
    num2 = num1 
    
    if num1 % num2 == 0:
        return _prime_number
    elif num1 % num2 ==1:
        print("problem")



