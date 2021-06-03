from datetime import date, timedelta

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
    date = date.today() + timedelta(days=3)
    dateString = date.strftime("%d-%m-%Y")
    newFileName = "Schedule for the week of " + dateString + ".txt"

    with open(newFileName, 'w') as fp:
        pass

    newFile = open(newFileName, "r+")

    newFile.truncate(0)
    peopleFile.truncate(0)
    newFile.close()
    peopleFile.close()

    index = (len(peopleList) - 1)
    tempPerson = peopleList[index]
    peopleList.pop(index)
    peopleList.insert(0, tempPerson)

    newFile = open(newFileName, "a")

    count = 0
    while count < len(peopleList):
        printString = rotationList[count] + " - " + peopleList[count]
        newFile.write(printString + '\n')
        print(printString)
        count += 1

    peopleFile = open("list of people in order.txt", "a")

    for i in peopleList:
        peopleFile.write(i + '\n')

    newFile.close()
    peopleFile.close()

else:
    print("Please check that the number of people in the file equals to the number of rotations.")
    peopleFile.close()