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

        users=[]
        users_id=[]
        for item in final:
            if item["user"]["id"] not in users_id:
                users_id.append(item["user"]["id"])
                users.append([item["user"]["id"], item["user"]["name"], 0])
            else:
                for it in users:
                    if it[0]==item["user"]["id"]:
                        it[2]+=1
        users.sort(key=lambda i: i[2], reverse=True)
        pprint(users)
