import json

def GroupBy(type, value, name):
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
        }
    }
    for meeting in categorizedMeetingData:
        if str(meeting[type]) == value:
            catResult[meeting["CategoryId"]]["Count"] += 1
            catResult[meeting["CategoryId"]]["Duration"] += meeting["Duration"]

    isDataValid = True
    for x in range(4):
        v = catResult[x]
        if ((v["Type"] == "SalesMeeting" and v["Duration"] > 30)
                or (v["Type"] == "TeamMeeting" and v["Duration"] > 40)
                or (v["Type"] == "Vacations" and v["Duration"] > 10)
                or (v["Type"] == "TeamActivity" and v["Duration"] > 10)
                or (v["Type"] == "Training" and v["Duration"] > 10)):
            isDataValid = isDataValid and True
        else:
            isDataValid = isDataValid and False

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