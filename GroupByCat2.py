import json
from random import randrange

def perc(val, total):
    return (val / total) * 100

def randomize(weight, r, val=0):
    return randrange(weight-r+val, weight+r+val)

def GroupBy(type, value, name, mock=True):
    userCategorizedFile = "CategorizedV2/{}.json".format(name)
    categorizedFile = open(userCategorizedFile, encoding='utf-8')
    categorizedMeetingData = json.load(categorizedFile)
    catResult = {
        0: {
            "Duration": 0,
            "Count": 0,
            "Type": "SalesMeeting"
        },
        1: {
            "Duration": 0,
            "Count": 0,
            "Type": "Vacations"
        },
        2: {
            "Duration": 0,
            "Count": 0,
            "Type": "TeamActivity"
        },
        3: {
            "Duration": 0,
            "Count": 0,
            "Type": "TeamMeeting"
        },
        4: {
            "Duration": 0,
            "Count": 0,
            "Type": "Training"
        },
        5: {
            "Duration": 0,
            "Count": 0,
            "Type": "Tool"
        }
    }
    for meeting in categorizedMeetingData:
        if str(meeting[type]) == value:
            catResult[meeting["CategoryId"]]["Count"] += 1
            catResult[meeting["CategoryId"]]["Duration"] += meeting["Duration"]

    isDataValid = True

    total = 0
    for x in range(6):
        v = catResult[x]
        total += v["Duration"]

    if total == 0:
        if type == "Day":
            total = 10
        elif type == "Week":
            total = 70
        elif type == "Month":
            total = 200
        elif type == "Year":
            total = 2500

    if mock:
        for x in range(6):
            v = catResult[x]
            if ((v["Type"] == "SalesMeeting" and perc(v["Duration"], total) >= 10)
                    and (v["Type"] == "TeamMeeting" and perc(v["Duration"], total) >= 40)
                    and (v["Type"] == "Vacations" and perc(v["Duration"], total) >= 10)
                    and (v["Type"] == "TeamActivity" and perc(v["Duration"], total) >= 10)
                    and (v["Type"] == "Training" and perc(v["Duration"], total) >= 10)):
                isDataValid = isDataValid and True
            elif v["Type"] == "Vacations" and perc(v["Duration"], total) >= 80:
                break
            else:
                isDataValid = isDataValid and False
                if v["Type"] == "SalesMeeting":
                    v["Duration"] = (randomize(15, 5, 2) / 10) * total
                elif v["Type"] == "TeamMeeting":
                    v["Duration"] = (randomize(20, 5, -3) / 10) * total
                elif v["Type"] == "Vacations":
                    v["Duration"] = (randomize(10, 5, -3) / 10) * total
                elif v["Type"] == "TeamActivity":
                    v["Duration"] = (randomize(15, 5) / 10) * total
                elif v["Type"] == "Training":
                    v["Duration"] = (randomize(10, 3) / 10) * total
                elif v["Type"] == "Tool":
                    v["Duration"] = (randomize(30, 5) / 10) * total

    return {
        "CatData": catResult,
        "isDataValid": isDataValid
    }


def GetUserInfo(name):
    userCategorizedFile = "CategorizedV2/{}.json".format(name)
    categorizedFile = open(userCategorizedFile, encoding='utf-8')
    categorizedMeetingData = json.load(categorizedFile)
    totalCount = {
        "Day": 0,
        "Week": 0,
        "Month": 0,
        "Year": 0
    }
    for meeting in categorizedMeetingData:
        for type in totalCount:
            totalCount[type] = totalCount[type] if totalCount[type] > meeting[type] else meeting[type]
    return totalCount