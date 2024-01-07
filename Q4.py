def ExpenseTracker():
    n = int(input("\n Enter the Salary Amount:"))
    def add_expense(expense,category,amount):
        print("Expense added")
    def display_expense(expense):
        print(f"{category}:{amount}")
    expense={}
    while True:

     print("\n 1. Add")
     print("\n 2. Display")
     print("\n 3. Exit")
     choice = input("\n Enter the choice (1,2,3) :")

     if choice ==1:
          category = input("\n Enter the  category:")
          amount = float(input("Enter the amount:"))
          add_expense(expense,category,amount)
     elif choice==2:
            display_expense(expense)
     elif choice ==3:
            print("Exiting Expense Tracker")
            break
     else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        




    '''print("\n a. Travel")
    print("\n b. Grocery")
    print("\n c. personal expense")
    x = input("\n Enter  the other expense :")
    a = int(input("\n Enter the travel expense:"))
    balence_amount = n - a''' 
    #print(f" \n The balence amount = {balence_amount}")

ExpenseTracker()



        


