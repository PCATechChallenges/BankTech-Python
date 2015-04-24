serialNumber = ""
while serialNumber == "":
    serialNumber = input("Please input the serial number to print:")

timesToPrint = 0
while timesToPrint == 0:
    someNumber = input("How many times should we print %s?" % serialNumber)
    if someNumber.isdigit():
        timesToPrint = int(someNumber)
    else:
        print("Please enter a valid number!")

for i in range(0, timesToPrint):
    print(serialNumber)

print("\n%s was printed %d times" % (serialNumber, timesToPrint))
