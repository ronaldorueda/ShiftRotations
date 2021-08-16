from myEmailSend import *
from rotations import *

UINum = 1

while (UINum != 0):
    print("1. Perform rotations and send email.")
    print("2. Perform rotations only and create file.")
    print("3. Perform rotations only and see it.")
    print("4. See current schedule/rotations.")
    print("0. Quit program.")
    print()
    UINum = int(input('Please enter your selection without the period: '))

    print()

    if (UINum == 1):
        fileName = performRotation()

        if('Schedule' in fileName):
            fileNameExt = fileName + ".txt"
            sendEmail(fileName, fileNameExt)
        else:
            print(fileName)

    elif (UINum == 2):
        fileName =  performRotation()
        
        if("Schedule" in fileName):
            print(fileName, " has been created.")
            print()
        else:
            print(fileName)
            print()

    elif (UINum == 3):
        peopleList = list()

        peopleList = getPeopleList()
        peopleList = rotatePeopleList(peopleList)

        scheduleList = getRotations()

        for i in scheduleList:
            print(i)

        print()

    elif (UINum == 4):
        print("Current current schedule/rotation.")

        scheduleList = getRotations()

        for i in scheduleList:
            print(i)

        print()

    elif (UINum == 0):
        print("Have a great day.")
        print()

    else:
        print("Please enter a proper number.")
        print()