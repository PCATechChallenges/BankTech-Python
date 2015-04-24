### Don't forget, Python needs all custom functions & imports to be defined BEFORE the main routine is actioned!
from math import sqrt

### Takes an int and returns true/false as to whether it is a prime number
def isPrime(numberToCheck):
    
    # 0 and 1 are NOT prime so we can ignore them
    # http://en.wikipedia.org/wiki/Prime_number
    if numberToCheck < 2: 
        return false

    # Any numbers divisible by 2 can't be prime, apart from the number 2.
    # Hey look! They all just happen to be EVEN NUMBERS! :D
    if numberToCheck % 2 == 0:
        return numberToCheck == 2 # This statement returns a true/false boolean when comparing whether numberToCheck is equal to 2

    # Only interested in odd numbers
    sqrtOfNumber  = int(sqrt(numberToCheck))
    for i in range(3, sqrtOfNumber, 2):
        
        # if the number is cleanly divisible by the current number in the range then it can't be prime!
        if numberToCheck % i == 0:
            return False

    # if we get this far, we've exhausted all numbers, so this MUST be prime! :D
    return True
### isPrime ENDS ###


### MAIN ROUTINE STARTS ###
print("Let's find some primes!!\n")

# Get the starting number
startNumber = 0
while startNumber <= 0:
    someNumber = input("What number should we start looking for primes from?: ")
    if someNumber.isdigit():
        startNumber = int(someNumber)
    else:
        print("Please enter a valid number!")

# Get the ending number
endNumber = 0
while (endNumber <= 0 or endNumber <= startNumber):
    someNumber = input("At what number should we stop looking?: ")
    if someNumber.isdigit():
        endNumber = int(someNumber)
    else:
        print("Please enter a valid number!")

# Cycle through the given range and check for primes
primeCounter = 0
for i in range(startNumber, endNumber):

    # By reversing the logical IF statement we can reduce the levels of code nesting
    if not isPrime(i): continue

    print(i)
    primeCounter += 1

print("There were %d prime numbers between %d and %d" % (primeCounter, startNumber, endNumber))
### MAIN ROUTINE ENDS ###


