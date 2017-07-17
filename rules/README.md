## Insert Rules into EXTRA

There are two sets of rules developed during EXTRA project. The first one is based on a set of documents from Thomson Reuters. The second set of rules one is based on documents for Austrian Press Agency. You can find these corpora [here](https://github.com/iptc/extra-examples/tree/master/corpora).

For each of these sets the rules provided in two form: a) a json file having the following structure

```json
{
  "rules" :[
    {...},
    {...},
    {...}
  ]
}
```
and b) a text file with each rule in a separate line of the file.

The following python script reads the later txt file, line by line, and creates a rule for each line by call a POST method:

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
        rule = json.loads(line)
        rule['taxonomy'] = taxonomy
        headers = {'Content-Type': 'application/json'}
        post_resp = requests.post((host + "/rules"), data=json.dumps(rule), headers=headers)
        if post_resp.status_code != 201:
            logging.error("[POST_RULE]Received non 200 response. Got {}".format(post_resp.status_code))
```

To import the rules run the [python script] :

```sh
$python insert_rules.py IPTC-Media-Topics-english.txt http://xxx.xxx.xxx.xxx:8888/extra/api taxonomy_id
```

You should specify the file containing the rules and also the entry point of EXTRA API (e.g. http://xxx.xxx.xxx.xxx:8888/extra/api). Also the id of the taxonomy created before must be specified as the third parameter of the script. 
