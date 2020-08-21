import json, random
from datetime import date

fortuneList = json.loads(open('fortunes.json').read())
nameList = json.loads(open('name.json').read())
date = date.today()
date = str(date)
month = ""
day = date[8] + date[9]
year = date[0] + date[1] + date[2] + date[3]
name = ""

def getName():
    global name
    name = input("What is your name?\n")
    with open('name.json', 'w') as nameFile:
        json.dump(name, nameFile)


if date[5] == str(0):
    if date[6] == str(1):
        month = "January"
    elif date[6] == str(2):
        month = "February"
    elif date[6] == str(3):
        month = "March"
    elif date[6] == str(4):
        month = "April"
    elif date[6] == str(5):
        month = "May"
    elif date[6] == str(6):
        month = "June"
    elif date[6] == str(7):
        month = "July"
    elif date[6] == str(8):
        month = "August"
    elif date[6] == str(9):
        month = "September"
else:
    if date[6] == str(0):
        month = "October"
    elif date[6] == str(1):
        month = "November"
    else:
        month = "December"


def main():
    fortune = random.choice(fortuneList)
    print("\nHello, " + nameList + "! " "Today is " + month + " " + day + ", " + year + ".\n")
    print("Your fortune is: " + "\"" + fortune + "\"\n")
if nameList == "":
    getName()
    nameList = name
main()