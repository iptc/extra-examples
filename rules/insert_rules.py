#!/usr/bin/python

import json
import sys
import requests
import logging

host = sys.argv[2]
input_file = sys.argv[1]
taxonomy = sys.argv[3]
with open(input_file) as f:
    for line in f:
        rule = json.loads(line)
        rule['taxonomy'] = taxonomy
        headers = {'Content-Type': 'application/json'}
        post_resp = requests.post((host + "/rules"), data=json.dumps(rule), headers=headers)
        if post_resp.status_code != 201:
            logging.error("[POST_RULE]Received non 200 response. Got {}".format(post_resp.status_code))
