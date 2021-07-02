from datetime import date, timedelta

def performRotation():
    peopleFile = open("list of people in order.txt", "r+")
    
    peopleList = getPeopleList()
    peopleList = rotatePeopleList(peopleList)
    rotationList = getRotationList()
    fileName = createFile()

    if(len(peopleList) == len(rotationList)):
        addRotationsToFile(peopleList, rotationList, fileName)
    else:
        print("Please check the rotaions list and people list to see if they are equal.")

def createFile():
    date = date.today() + timedelta(days=3)
    dateString = date.strftime("%m-%d-%Y")
    fileName = "Schedule for week of " + dateString

    return fileName

def addRotationsToFile(peopleList, rotationList,fileName):
    fileNameExt = fileName + ".txt"

    with open(fileNameExt, 'w') as fp:
        pass

    newFile = open(fileNameExt, "r+")

    count = 0

    while count < len(peopleList):
        newString = rotationList[count] + " - " + peopleList[count]
        newFile.write(newString + '\n')
        count += 1

    newFile.close()

def getRotationList():
    rotationFile = open("rotations.txt")
    
    rotationList = list()

    for line in rotationFile:
        temp = line.rstrip()
        rotationList.append(temp)

    rotationFile.close()

    return rotationList

def getPeopleList():
    peopleFile = open("list of people in order.txt")

    peopleList = list()

    for line in peopleFile:
        temp = line.rstrip()
        peopleList.append(temp)

    peopleFile.close()

    return peopleList()

def rotatePeopleList(peopleList):
    index = (len(peopleList) - 1)
    tempPerson = peopleList[index]
    peopleList.pop(index)
    peopleList.insert(0, tempPerson)

    peopleFile = open("list of people in order.txt", "r+")
    peopleFile.truncate(0)
    peopleFile.close()

    peopleFile = open("list of people in order.txt", "a")

    for i in peopleList:
        peopleFile.write(i + '\n')
    
    peopleFile.close()