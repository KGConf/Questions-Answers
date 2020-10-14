import json

import requests # apt-get install python-requests
# based on https://github.com/discoursehosting/discourse-api-php/blob/master/lib/DiscourseAPI.php

# log all the things so you can see what's going on
import logging
import http.client as httplib
if __name__ == '__main__':

    httplib.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    with open('./discourse-api-key.txt') as f:
	    apikey = f.readline()
    APIKEY = apikey
    APIUSERNAME = "admin"
    QSPARAMS = {"api-key": APIKEY, "api-username": APIUSERNAME, "Accept": "application/json"}
    FORUM = "https://answers.knowledgegraph.tech/"  # with the slash on the end

    # First, get cookie
    r = requests.get(FORUM, headers=QSPARAMS)
    SESSION_COOKIE = r.cookies #["_forum_session"]

    # Now, send a post to the _forum_session
    post_details = {
        "title": "Title of the new topic",
        "raw": "Body text of the post",
        "category": 1,
        "archetype": "regular",
        "reply_to_post_number": 0
    }
    r = requests.post(FORUM + "posts", headers=QSPARAMS, data=post_details)
    print("Various details of the response from discourse")
    print(r.headers)
    #print(r.text, r.headers, r.status_code)
    #disc_data = json.loads(r.text)
    #disc_data["FORUM"] = FORUM
    #print("The link to your new post is: ")
    #print("%(FORUM)st/%(topic_slug)s/%(topic_id)s" % disc_data)
