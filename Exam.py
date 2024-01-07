# 1. write a program to display the last number of the digit.
'''user_input=int(input("Enter the number:"))
last_digit=0
if user_input > 0:
    last_digit=user_input%10
print(f"The last digit of the number is {last_digit}")'''


# 2. write a program to accept percentage from the user an display the grade according to the following criteria.
'''user_input = int(input("Enter the input:"))
if user_input >=90:
    print("A")
elif user_input >=80 and user_input <=90:
    print("B")
elif user_input >=60 and user_input <=80:
    print("C")
elif user_input <=60:
    print("D")
else:
    print("Invalid")'''



# 3. write a program to check whether given number is diivsible by 3 or not.
'''user_input=int(input("Enter a number: "))
if user_input %3==0:
    print(f" the number is  divisible by {user_input}")
else:
    print(f"The number is not divisible by {user_input}")'''


# 4. write a program to display "Hello" if a number entered by user is a multiple of five otherwise print "Bye".
'''user_input=int(input("Enter a number:"))
if user_input%5==0:
    print("Hello")
else:
    print("Bye")'''

# 5. write a program to acept the cost  price of a bike and display the road tax to be paid accordingly.
user_input = int(input("Enter the input:"))
if user_input>100000:
    tax=user_input*(15/100)
elif user_input>50000 and user_input<=100000:
    tax=user_input*(10/100)
else:
    tax=user_input*(5/100)
print("Tax =",tax)


# 6. write a program to calculate the electricity bill according to the following criteria:
'''user_input = int(input("Enter the unit:"))
if user_input<100:
    amount = 0
elif user_input > 100 and user_input <= 200:
    a = 200-user_input
    amount = (100*0)+((100-a)*5)
else:
    a = user_input-200
    amount = (100*5)+(a*10)

print(f"The bill is :{amount}")'''


# 7. write a program to accept a number from 1 to 7 and display the name of the day like 1 day for sunday, 2 for monday and so on.
'''user_input = int(input("Enter the input from 1 to 7 :"))
if user_input ==1:
    print("Sunday")
elif user_input ==2:
    print("Monday")
elif user_input ==3:
    print("Tuesday")
elif user_input ==4:
    print("Thurday")
elif user_input ==5:
    print("Friday")
elif user_input ==6:
    print("Saturday")
else:
    print("Invalid")'''


# 8. write the output of the program.

'''a=int(input("Enter the input:"))
if (a>5 and a<=10):
    print("Hello")
else:
    print("Bye")'''

# 9. write a program to accept a number from 1 to 12 and display the name of the month and day in month like 1 for january and numbers of days 31 and so on
'''user_input = int(input("Enter input from 1 to 12:"))
if user_input ==1:
 print("January")
elif user_input ==2:
 print("February")
elif user_input ==3:
 print("March")
elif user_input ==4:
 print("April")
elif user_input ==5:
 print("May")
elif user_input ==6:
 print("June")
elif user_input ==7:
 print("July")
elif user_input ==8:
 print("Augest")
elif user_input ==9:
 print("September")
elif user_input ==10:
 print("October")
elif user_input ==11:
 print("Novemer")
elif user_input ==12:
 print("December")
else:
  print("Invalid")'''
# 10. Accept any city from the user and display monument of that city
'''user_input = input("Enter the input:")
if user_input == "Delhi":
    print("Red fort")
elif user_input == "Agra":
    print("Taj mahal")
elif user_input == "Jaipur":
    print("Jal mahal")'''