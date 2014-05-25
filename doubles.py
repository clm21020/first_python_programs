print("This program doubles numbers between 0 and 10")
while(True):
    user_input = raw_input("Enter a number between 0 and 10: ")
    if int(user_input) >0 and int(user_input) <10:
        print( str(2* int(user_input)) + " is the double of your number")
    else:
        print("The value entered was not a number between 0 and 10. Please try again.")
