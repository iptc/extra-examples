# extra-examples

Examples for the IPTC EXTRA classification engine.
This repository contains the objects/resources that can be used to validate the proper functionality of IPTC EXTRA project.

See the other repositories of the IPTC EXTRA project:

* https://github.com/iptc/extra-core
* https://github.com/iptc/extra-ext


There are five types of resources: rules, schemas, taxonomies, topics and corpora of documents. After a successful deployment of EXTRA Toolkit, following the guide you can find in the [extra-ext](https://github.com/iptc/extra-ext) repository, these objects should be inserted into the platform.

**Note!** You can import all the resources by running [this](https://github.com/iptc/extra-examples/blob/master/insert_resources.py) python script.

```sh
$ python insert_resources.py params.json
```
The only change you need to make is to add the directory of the documents (`documents_file`) in the [params.json](https://github.com/iptc/extra-examples/blob/master/params.json) file. To get the document please fill the form you can find [here](https://github.com/iptc/extra-examples/tree/master/corpora).  

## Taxonomies and Topics
In the current version of EXTRA, there are two taxonomies with their corresponding topics. More specifically, the two taxonomies are [IPTC's Media Topics](https://github.com/iptc/extra-ext) in english and german respectively.

To create these taxonomies in EXTRA use the corresponding EXTRA API method:

**POST** */taxonomies*
```json
{
  "language": "english",
  "name": "IPTC Media Topics"
}
```

**POST** */taxonomies*
```json
{
  "language": "german",
  "name": "IPTC Media Topics"
}
```

Upon successful creation, each of these methods will return the newly created taxonomy with a unique taxonomy id. For example:

**Response**

*201 - Created*
```json
{
  "id": "5901b9e5c41479000146ced2",
  "language": "english",
  "name": "IPTC Media Topics"
}
```

To create topics in a taxonomy e.g. in the taxonomy with id=5901b9e5c41479000146ced2 created before:

**POST** */taxonomies/5901b9e5c41479000146ced2/topics*
```json
{
  "taxonomyId": "5901b9e5c41479000146ced2",
  "name": "arts, culture and entertainment",
  "definition": "Matters pertaining to the advancement and refinement of the human mind, of interests, skills, tastes and emotions ",
  "topicId": "medtop:01000000"
}
```

To insert these two taxonomies and their corresponding topics use the script files and the guide can be found [here](https://github.com/iptc/extra-examples/tree/master/topics).

## Schemas

To create a new schema in EXTRA:

**POST** */schemas*

```json
{
  "name":"Apa Schema",
  "fields":[
    {"name":"title", "hasParagraphs":false, "hasSentences":true, "textual":true},
    {"name":"subtitle", "hasParagraphs":false, "hasSentences":true, "textual":true},
    {"name":"body", "hasParagraphs":true, "hasSentences":true, "textual":true},
    {"name":"id", "hasParagraphs":false, "hasSentences":false, "textual":false},
    {"name":"slugline", "hasParagraphs":false, "hasSentences":false, "textual":false},
    {"name":"versionCreated", "hasParagraphs":false, "hasSentences":false, "textual":false}],
    "language":"german"
}
```

In EXTRA there are two schemas one for articles from Thomson Reuters and one for Austrian Press Agency. You can see these schemas [here](https://github.com/iptc/extra-examples/blob/master/schemas/schemas.json).

## Corpora

To create a new corpus that follows a specific schema and its documents are annotated with the topics of a specific taxony:

**POST** */corpora*

```json
{
  "name": "Apa Corpus",
  "language": "german",
  "schemaId": "591f070c30c49e00011de8eb" ,
  "taxonomyId": "5901b9ebc41479000146ced3"
}
```

To index documents, for developement and testing of rules, into the newly created corpus, follow the guide [here](https://github.com/iptc/extra-examples/tree/master/corpora).

## Rules

To create a new rule for a given taxonomy and a topic within that taxonomy:

**POST** */rules*

```json
{
	"name": "Test Rule",
	"query": "(or (and (title adj/regexp \"\\d+\\-?\\s+?year\\-?\\s?old\") (body any/stemming \"boy child children girl infant juvenile kid newborn schoolboy schoolgirl toddler\") ) (and (title adj/regexp \"\\d+\\-?\\s+?month\\-?\\s?old\") (body any/stemming \"boy child children girl infant juvenile kid newborn schoolboy schoolgirl toddler\") ) )",
	"taxonomy": "5901b9e5c41479000146ced2",
	"topicId": "medtop:20000790"
}
```

The taxonomy id and the topic id must correspond to resources that have already created into the platform.
The rules developed during EXTRA project can be found [here](https://github.com/iptc/extra-examples/tree/master/topics). To insert them into EXTRA use the script and follow the corresponding guide [here](https://github.com/iptc/extra-examples/tree/master/rules).


## Contact for further details about the project

Technical details: Manos Schinas (manosetro@iti.gr), Symeon Papadopoulos (papadop@iti.gr)

Project as a whole: [IPTC](https://iptc.org) (office@iptc.org)
