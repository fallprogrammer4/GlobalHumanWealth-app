import math

# Variables for user information and balance
name = ""  # username
pin = ""   # password
cb = 0    # current balance

# Welcome message
print("Welcome to Global Human Wealth online banking")
print("Select a number to choose an option, otherwise please enter info")

# Signup page
def signup():
    global name, pin, cb  # Use global variables
    name = input("Please create your username: ")
    pin = input("Please create your six-digit pin: ")

    if len(pin) != 6:
        print("Invalid! Pin must be six digits.")
        signup()
    else:
        print("Sign up successful")
        print("Thanks for creating your account")
        print("Welcome " + name + "! Glad you chose G.H.W Banking app.")

# Forgot Pin
def forgotpin():
    global pin
    recoverpin = input("Please create your new six-digit pin: ")
    if len(recoverpin) != 6:
        print("Invalid! Pin must be six digits.")
        forgotpin()
    else:
        pin = recoverpin
        print("New pin has been restored")
        print("Please login")
        login()

# Deposit interest calculation
def depositinterest(p, r, t):
    p = float(p)
    r = float(r)
    t = float(t)
    a = p * math.exp(r * t)
    return a

# User login
def login():
    global cb
    name1 = input("Please enter your username: ")
    pin1 = input("Please enter your pin: ")

    if name1 == name and pin1 == pin:
        print("Welcome to G.H.W online banking, " + name)
        print("What can we assist you with today?")

        # Menu options
        menu = [
            '1- Deposit',
            '2- Withdraw',
            '3- Transfer',
            '4- Check Balance',
            '5- Deposit Interest',
            '6- Calculate Compound Interest'
        ]

        for option in menu:
            print(option)

        choice = int(input("Select an option: "))

        if choice == 1:
            deposit_amount = int(input("Enter the amount to deposit: "))
            cb += deposit_amount
            print("Your current balance is now $" + str(cb))

        # Implement other menu options here...

    else:
        print("Username or Pin is invalid")
        print("Did you create your account?")
        list1 = ["1- Yes", "2- No"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice: "))
        if inp == 1:
            list2 = ["1- Can you please login again?", "2- Forgot pin?"]
            for e in list2:
                print(e)
            answer = int(input("Enter your choice please"))
            if answer == 1:
                login()
            elif answer == 2:
                menu()
            else:
                print("Unavailable Option")
                login()
        elif inp == 2:
            print("Create your account")
            signup()

# Main menu
def mainmenu():
    optionone = int(input("Choose 1 to sign up and Choose 2 to log in: "))
    if optionone == 1:
        signin()
    elif optionone == 2:
        login()  # Call the login function
    else:
        print("Option is not available")

    exit_choice = input("Are you finished? (Yes or No) ")
    if exit_choice.lower() == "no":
        mainmenu()
    elif exit_choice.lower() == "yes":
        print("Thank you for using G.H.W online banking")
    else:
        print("Option is not available")

# Start the main menu
mainmenu()
