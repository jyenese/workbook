# raining but temp is less then 15 degrees = "Its wet and cold"
# Less than 15 degrees but isnt raining = "ITs not raining but cold"
# Greater than or equal to 15 but no rainining = "Its warm but no raining"
# otherwise "its warm and raining"


raining = input("Is it raining?:")  
temperature = int((input("How hot is it in degrees? ")))
if temperature < 15 and raining == "yes":
    print("it's wet and cold")
elif temperature < 15 and raining == "no":
    print("It's not raining but cold.")
elif temperature >= 15 and raining == "no":
    print("Its warm but no raining")
else:
    print("its warm and raining")
    

