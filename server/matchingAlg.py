import json
import pymongo
from pymongo import MongoClient
import operator
from pprint import pprint
import personality
from database import add_user, update_user

client = MongoClient('mongodb://107.170.2.182:27017/')
diffarray = []

def sortingal (alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position -1]
            position = position - 1

        alist[position] = currentvalue

        return alist

def personalitytest(document, document1):
    personality = document["personality"]
    personality1 = document["personality"]

    person_num = []
    person1_num = []

    sum_diff_percent = 0.0

    for i in range(0,5):
        for j in range(0,6):
            person_num.append(personality[i]["children"][j]["percentile"])
            person1_num.append(personality1[i]["children"][j]["percentile"])

    for k in range (0,30):
        sum_diff_percent = sum_diff_percent + abs(person_num[k] - person1_num[k])

    diffarray.append(sum_diff_percent)
    print(diffarray)

def matchingal(email):
    type_bud = ''
    db = client.buddy
    collection = db['users']
    cursor = collection.find({})
    for document in cursor:#dictionary at this point
        print(document)
        if(document["email"] == email):
            type_bud = document["interest"]["type"]

    for document1 in cursor:
        if (document1["interest"]["type"] == type_bud):
            if (type_bud.ascii_lowercase == 'study'):
                if (document1["interest"]["department"] == document["interest"]["department"] and document1["interest"]["number"] == document["interest"]["number"]):
                    personalitytest(document,document1)
            elif (type_bud.ascii_lowercase == 'travel'):
                if (document1["interest"]["city"] == document["interest"]["city"] and document1["interest"]["country"] == document["interest"]["country"]):
                    personalitytest(document,document1)
            elif (type_bud.ascii_lowercase == 'language'):
                if (document1["interest"]["learn"] == document["interest"]["teach"] and document1["interest"]["teach"] == document["interest"]["learn"]):
                    personalitytest(document,document1)
            elif (type_bud.ascii_lowercase == 'gaming'):
                if (document1["interest"]["game"] == document["interest"]["competitiveness"] and document1["interest"]["game"] == document["interest"]["competitiveness"]):
                    personalitytest(document,document1)

matchingal("kkanwar2@illinois.edu")
