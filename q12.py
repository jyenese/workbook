# First of all there was no text in the input, so it was asking for nothing in terminal. (This actually doesn't matter but it always helps.)(It will still give an answer.)
# Secondly when asking for a number, 
# Converted celsius to a float, because when asking for a number in the string, you need to convert with int or float.

celsius = float(input("Insert text here"))

fahrenheit = (celsius*9/5)+32

print(f"The result is: {fahrenheit}.")

