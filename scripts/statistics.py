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

    with open('pos.csv', 'w', newline='') as f1:

            w1 = csv.writer(f1)
            w1.writerow(["title", "author", "author_rep_score", "tags" ])
            tag_stats = {}
            count=0
            lines = 0
            for item in final:
                for tag in item["tags"]:

                    if tag not in tag_stats.keys():
                        tag_stats[tag] = 0
                    else:
                        tag_stats[tag] += 1
                if item["tags"] == []:
                    count += 1

                if item["score"]>0:
                    w1.writerow([item["title"], item["user"]["name"],  item["user"]["reputation"], item["tags"] ])
                    lines+=1


            print(lines)
            f1.close()
            sorted_x = sorted(tag_stats.items(), key=operator.itemgetter(1), reverse=True)
            sorted_x=[ i for i in sorted_x if i[1]>0]
            print(len(sorted_x))
            print(lines)
            pprint(sorted_x)


            labels, ys = zip(*sorted_x)
            xs = np.arange(len(labels))
            width = 0.5

            fig = plt.figure()
            ax = fig.gca()  # get current axes
            ax.bar(xs, ys, width, align='center')

            # Remove the default x-axis tick numbers and
            # use tick numbers of your own choosing:
            ax.set_xticks(xs)
            ax.set_xticklabels(labels)
            # Remove the default y-axis tick numbers and
            # use tick numbers of your own choosing:
            ax.set_yticks(ys)
            plt.yticks(fontsize=7 )
            plt.xticks(rotation=90, fontsize=6)
            fig.suptitle('Most frequent tags for negatively or zero scored questions (t=100)', fontsize=12)
            plt.savefig('negscore.png')