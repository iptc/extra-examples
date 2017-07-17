## Insert Topics into EXTRA

There are two sets of topics used in EXTRA project, correspond to the english and german version of IPTC's [Media Topics](https://iptc.org/standards/media-topics/).

For each of these sets the topics provided in two form: a) a json file having the following structure

```json
{
  "topics" :[
    {
      "definition": "...",
      "label": "...",
      "name": "...",
      "topicId": "..."
    },
    {...},
    {...}
  ]
}
```
and b) a text file with each topic in a separate line of the file.



Let's say we want to create the English version of Media Topics taxonomy. First we have to create the corresponding taxonomy:

The following python script reads the txt file, line by line, and creates a topic for each line by call the corresponding POST method:

```python
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
        topic = json.loads(line)
        topic['taxonomyId'] = taxonomy
        headers = {'Content-Type': 'application/json'}
        url = host + '/taxonomies/' + taxonomy + '/topics'
        post_resp = requests.post(url, data=json.dumps(topic), headers=headers)
        if post_resp.status_code != 201:
            logging.error("[POST_TOPIC] Received non 200 response. Got {}".format(post_resp.status_code))
```

To import the topics run this [python script](https://github.com/iptc/extra-examples/blob/master/rules/insert_topics.py):

```sh
$python insert_topcis.py IPTC-Media-Topics-english.txt http://xxx.xxx.xxx.xxx:8888/extra/api taxonomy_id
```
You should specify the file containing the topics and also the entry point of EXTRA API (e.g. http://xxx.xxx.xxx.xxx:8888/extra/api). Also we assume that the taxonomy is already created.

To create a taxonomy in python e.g. the german media Topics:

```python
#!/usr/bin/python

import json
import requests
import logging

host = "http://xxx.xxx.xxx.xxx:8888/extra/api"
taxonomy = { "language": "german", "name": "IPTC Media Topics"}
#taxonomy = { "language": "english", "name": "IPTC Media Topics"}

headers = {'Content-Type': 'application/json'}
post_resp = requests.post(host + '/taxonomies', data=json.dumps(taxonomy), headers=headers)
if post_resp.status_code != 201:
    logging.error("[POST_TAXONOMY] Received non 200 response. Got {}".format(post_resp.status_code))
else:
    logging.info(print(post_resp.json()['id']))
```
