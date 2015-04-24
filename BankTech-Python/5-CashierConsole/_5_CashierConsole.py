### Simple function to subtract from a given balance and return the resulting balance
def subtractFromBalance(balance):
    sumToSubtract = 0
    while sumToSubtract <= 0:
        someNumber = input("How much would you like to SUBTRACT? ")
        if someNumber.isdigit():
            sumToSubtract = int(someNumber)
        else:
            print("Please enter a valid number!")

    balance -= sumToSubtract
    print("Subtracted %d" % sumToSubtract)
    return balance


### Simple function add to the given balance and return the resulting balance
def addToBalance(balance):
    sumToAdd = 0
    while sumToAdd <= 0:
        someNumber = input("How much would you like to ADD? ")
        if someNumber.isdigit():
            sumToAdd = int(someNumber)
        else:
            print("Please enter a valid number!")

    balance += sumToAdd
    print("Added %d" % sumToAdd)
    return balance


### MAIN SEQUENCE STARTS ###

print("Welcome to Bank Tech's Cashier System!\n#######################################\n")

# Get the customer's balance
balance = 0
while balance <= 0:
    someNumber = input("What is the customer's starting balance? ")
    if someNumber.isdigit():
        balance = int(someNumber)
    else:
        print("Please enter a valid number!")

# Perform some actions on the account
while True:

    # Get an input to perform an action
    action = ""
    while action == "":
        action = input("Current balance is: %d\n Press 'A' to add more funds or 'S' to subtract from the balance or 'X' to exit:" % balance)

    # Exit the program if the user typed an x or X
    if action.upper() == "X": break

    # call the addToBalance Function if a or A is pressed
    if action.upper() == "A": 
        balance = addToBalance(balance)
        
    # call the subtractFromBalance Function if s or S is pressed
    elif action.upper() == "S": 
        balance = subtractFromBalance(balance)

    # handle any bad keystrokes
    elif(action.upper() != "X" and action.upper() != "A" and action.upper() != "S"): print("Command not recognised. Please try again")

print("\nSession complete.\nHave a nice day :)")