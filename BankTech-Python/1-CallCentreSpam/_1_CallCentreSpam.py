phoneList = open("PhoneList.txt", "r")

goodCount = 0
spamCount = 0

for phoneNumber in phoneList:
    if "SPAM" in phoneNumber:
        print("SPAM")
        spamCount += 1
    else:
        print("OK")
        goodCount += 1

print("%s numbers processed.\n%s SPAM numbers found.\n%s numbers were OK" % (goodCount + spamCount, spamCount, goodCount))