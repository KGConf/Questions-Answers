

import json

import requests # apt-get install python-requests
import discourse
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

        SESSION_COOKIE = r.cookies  # ["_forum_session"]

        with open('./api-user-passwords.txt') as f:
            pwd = f.readline()

        # Now, create a user to the _forum_session

        user_details = {

            "name": "pippo",

            "email": "pippo@email.invalid",

            "password": pwd,

            "username": "pippo",

            "active": True,

            "approved": True,

            "user_fields[1]": "string"

        }

        r = requests.post(FORUM + "users", headers=QSPARAMS, data=user_details)

        print("Various details of the response from discourse")

        print(r.text["success"])




