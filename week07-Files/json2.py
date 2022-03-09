#storing sample dict to a file as JSON
import json
filename = "testdict.json"
sample = dict(name ='fred', age=31, grades=[1,34,55])

def writeDict(obj):
    with open (filename, 'wt') as f:
        json.dump(obj,f)

writeDict(sample)

#this as created a dict file in json format 