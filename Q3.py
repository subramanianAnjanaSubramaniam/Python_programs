# write a python program that execute an opertaion on a list and handles an  Indexerror exception if he index is out of range.
def ee():
    try:
        numbers = []
        myList = int(input("Enter the limit:"))
        print("Enter the number:")
        for i in range(0,myList):
                num = int(input())
                numbers.append(num)
        print(numbers)
        a = int(input("Enter an index:"))
        print(numbers[a])

    except IndexError:
        print(" Index Error list is out of range")
ee()