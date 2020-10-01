import json
import csv
from pprint import pprint
import re
from html import unescape

TAG_RE = re.compile(r'<[^>]+>')

html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
        }
def html_escape(text):
  """Produce entities within text."""
  return "".join(html_escape_table.get(c,c) for c in text)
def remove_tags(text):
    return TAG_RE.sub('', text)

if __name__ == '__main__':

    with open("questions.json", 'r') as f:
        # read the data
        final = json.load(f)["questions"]
        f.close()
    with open('entries.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "Title", "Content", "Tags", "Answer"])
        for i in range(len(final)):
            answer_pool=[]
            for j in range(len(final[i]["answers"])):
                answer_pool.append(remove_tags(unescape(final[i]["answers"][j]["content"])).replace("\n", ""))
            writer.writerow([i+1, final[i]["title"], remove_tags(unescape(final[i]["content"])), final[i]["tags"], answer_pool])
