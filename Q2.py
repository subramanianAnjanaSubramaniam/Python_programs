# write a python program that prompts the user to input an integer and raise a valueError exception if the input is not a valid integer
try:
    user_input = int(input("Enter the number:"))
    print(user_input)
  
except ValueError:
    raise Exception("floating point number is not consider as integer")