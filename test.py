testFile = open("Z:\schedule.txt", "r")

scheduleList = list()

for line in testFile:
    temp = line.rstrip()
    scheduleList.append(temp)

testFile.close()

for i in scheduleList:
    print(i)