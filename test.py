from datetime import date, timedelta

newFileName = ""

date = date.today() + timedelta(days=3)
datestring = date.strftime("%m-%d-%Y")

newFileName = newFileName + "test-" + datestring + ".txt"

with open(newFileName, 'w') as fp:
    pass
