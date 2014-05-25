while(True):
    user_input = raw_input('What is your favorite color? ')
    if user_input.upper() == 'PLEASE STOP':
        break

    if user_input.upper() == 'BLUE':
        print("You're Awesome!")
    else:
        print("You Suck!")
