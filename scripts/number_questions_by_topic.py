import json
from pprint import pprint
import operator

if __name__ == '__main__':
    tag_list = []
    rank={}
    with open("questions.json", 'r') as fp:
        # read the data
        final = json.load(fp)["questions"]
        fp.close()
    with open("tags.txt") as f:
        [tag_list.append(line.rstrip('\n')) for line in f]
        f.close()
    for item in final:
        for tag in item["tags"]:
            if tag not in rank.keys():
                rank[tag]=1
            else:
                rank[tag]+=1
    sorted_x = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)
       