peopleFile = open("list of people in order.txt", "r+")
rotationFile = open("rotations.txt")

    #rotationList = rotationFile.readlines()
    #peopleList = peopleFile.readlines()

peopleList = list()
rotationList = list()

for line in peopleFile:
    temp = line.rstrip()
    peopleList.append(temp)

for line in rotationFile:
    temp = line.rstrip()
    rotationList.append(temp)

rotationFile.close()

if (len(peopleList) == len(rotationList)):
    peopleFile.truncate(0)

    index = (len(peopleList) - 1)
    tempPerson = peopleList[index]
    peopleList.pop(index)
    peopleList.insert(0, tempPerson)

    peopleFile.close()

    count = 0
    while count < len(peopleList):
        printString = rotationList[count] + " - " + peopleList[count]
        print(printString)
        count += 1

    peopleFile = open("list of people in order.txt", "a")

    for i in peopleList:
        peopleFile.write(i + '\n')

    peopleFile.close()

else:
    print("Please check that the number of people in the file equals to the number of rotations.")
    peopleFile.close()