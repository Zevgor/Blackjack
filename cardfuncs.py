import json
import random

def read_file(filepath):
    with open(filepath) as f:
        return json.load(f)

def cardsleft(inpdict):
    count=0
    for v in inpdict:
        count=count+1
    print(count,'cards left')

def drawanother(inplist):
    cardN = inplist.pop(random.randint(0, len(inplist)-1))
    return cardN

def calcvalue(inphand):
    value = 0
    for k in inphand:
        value += k["bjval"]
    if value > 21:
        for k in inphand:
            if k["value"] == 'Ace':
                if k["bjval"] == 11:
                    k["bjval"] = 1
                    value = calcvalue(inphand)
                    break
    return value