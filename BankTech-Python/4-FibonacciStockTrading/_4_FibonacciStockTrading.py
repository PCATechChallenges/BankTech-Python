### Fibonacci sequence is always the same
### Generate the sequence up to the starting point and then store the required amount to return
def generateFibs(checkpoint, numbersAfter):
    # Fn = Fn-1 + Fn-2
    F_n = []
    F_n_1 = 1
    F_n_2 = 0
    listIndex = 0

    while len(F_n) != (numbersAfter + 1):

        # Base calculation for a Fibonacci number
        fibNumber = F_n_1 + F_n_2

        # If we've reached our starting number, store the fib number
        if fibNumber >= checkpoint: 
            F_n.insert(listIndex, fibNumber)
            listIndex += 1

        # Increment the Fib sequence to the next number
        F_n_2 = F_n_1
        F_n_1 = fibNumber

    return F_n
### generateFibs() END ###


### MAIN ROUTINE STARTS ###
print("Let's find some Fibs!")

startNumber = 0
while startNumber <= 0:
    someNumber = input("Please enter a starting number to find within the Fibonacci sequence: ")
    if someNumber.isdigit():
        startNumber = int(someNumber)
    else:
        print("Please enter a valid integer!")
            
    
numberOfFibsToReturn = 0
while numberOfFibsToReturn <= 0:
    someNumber = input("How many Fib numbers should be returned after the starting value?: ")
    if someNumber.isdigit():
        numberOfFibsToReturn = int(someNumber)
    else:
        print("Please enter a valid integer!")

fibNumbers = generateFibs(startNumber, numberOfFibsToReturn)

for fib in fibNumbers:
    print(fib)

print("The first available Fib number after %d was %d" % (startNumber, fibNumbers[0]))
### MAIN ROUTINE ENDS ###