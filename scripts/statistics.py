import json
from pprint import pprint
import csv
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
        eq_0=[]
        eq_neg=[]
        count_eq_0=0
        count_less_0=0
        count_gen = 0
        for item in final:
            count_gen += 1
            if item["score"]<0:
                w2.writerow([item["title"], item["user"]["name"],  item["user"]["reputation"], item["tags"] ])
            elif item["score"]==0:
                w1.writerow([item["title"], item["user"]["name"],  item["user"]["reputation"],item["tags"] ])
        print((len(eq_0)/count_gen)*100)
        print((len(eq_neg)/count_gen)*100)
        f1.close()
        f2.close()

        pprint(eq_0)
        pprint(eq_neg)
