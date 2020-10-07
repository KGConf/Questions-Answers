import json
from pprint import pprint
import csv
import operator
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    with open("questions.json", 'r') as f:
        # read the data
        final = json.load(f)["questions"]
        f.close()

    with open('zero_scored_questions.csv', 'w', newline='') as f1, open('neg_scored_questions.csv','w', newline='' ) as f2:
            w1 = csv.writer(f1)
            w1.writerow(["title", "author", "author_rep_score", "tags" ])
            w2 = csv.writer(f2)
            w2.writerow(["title", "author", "author_rep_score", "tags" ])

            tag_stats = {}


            for item in final:
                for tag in item["tags"]:
                    if tag not in tag_stats.keys():
                        tag_stats[tag]=0
                    else:
                        tag_stats[tag]+=1
                if item["score"]<0:
                    w2.writerow([item["title"], item["user"]["name"],  item["user"]["reputation"], item["tags"] ])
                elif item["score"]==0:
                    w1.writerow([item["title"], item["user"]["name"],  item["user"]["reputation"],item["tags"] ])

            f1.close()
            f2.close()
            sorted_x = sorted(tag_stats.items(), key=operator.itemgetter(1), reverse=True)

            sorted_x = [ i for i in sorted_x if i[1]>10]
            pprint(sorted_x)

            x = np.array([ i[1] for i in sorted_x ])
            label = [i[0] for i in sorted_x ]


            plt.pie(x, labels=label)
            plt.show()