peopleFile = open("list of people in order.txt")
rotationFile = open("rotations.txt")

peopleList = list()
rotationList = list()

for line in peopleFile:
    temp = line.rstrip()
    peopleList.append(temp)

for line in rotationFile:
    temp = line.rstrip()
    rotationList.append(temp)

if (len(peopleList) == len(rotationList)):
    peopleFile.close()
    rotationFile.close()

    count = 0
    while count < len(peopleList):
        printString = rotationList[count] + " - " + peopleList[count]
        print(printString)
        count += 1

else:
    print("Please check that the number of people in the file equals to the number of rotations.")