from rotations import *
from myEmailSend import *

fileName = performRotation()

if('Schedule' in fileName):
    fileNameExt = fileName + ".txt"
    sendEmail(fileName, fileNameExt)
else:
    print(fileName)