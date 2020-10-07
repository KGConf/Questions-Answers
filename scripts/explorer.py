import json
import csv
from pprint import pprint
import re
from html import unescape
import operator
if __name__ == '__main__':
    with open("questions.json", 'r') as f:
        # read the data
        final = json.load(f)["questions"]
        f.close()
    users = []
    user_ids=[]

    for item in final:
        if item["user"]["id"] not in user_ids:
            user_ids.append(item["user"]["id"])
            users.append([item["user"]["id"], item["user"]["name"],item["user"]["reputation"]])
        for ans in item["answers"]:
            if ans["user"]["id"] not in user_ids:
                user_ids.append(ans["user"]["id"])
                users.append([ans["user"]["id"], ans["user"]["name"], ans["user"]["reputation"]])
    users.sort(key=lambda x: int(x[2]))
    users.reverse()
    commenters={}
    for id in user_ids:
        if id not in commenters.keys():
            commenters[str(id)]=0

    for item in final:
        for ans in item["answers"]:
            if str(ans["user"]["id"]) in commenters.keys():
                commenters[str(ans["user"]["id"])]+=1
    sorted_x = sorted(commenters.items(), key=operator.itemgetter(1), reverse=True)
    pprint(sorted_x)



