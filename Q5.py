# write a python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input
def KeyboardInterruptError():
    try:
        a = input("Enter the input:")
        
    except KeyboardInterrupt:
        print("Keyboard interrupt error")
KeyboardInterruptError()