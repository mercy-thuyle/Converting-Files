"""
Pickle2JSON is a simple Python Command Line program for converting Pickle file to JSON file.
Arguments: Only one (1) argument is expected which is the pickle file.
Usage: python pickle2json.py myfile.pkl
Output: The output is a JSON file bearing the same filename containing the JSON document of the converted Pickle file.
"""
# Source: https://gist.github.com/romgapuz/c7a4cedb85f090ac1b55383a58fa572c

# import libraries
import pickle
import json
import sys
import os



# open pickle file
print ("...Reading file.pkl")
with open(sys.argv[1], 'rb') as infile:
    pickle_obj = pickle.load(infile)

# convert pickle object to json object
print ("...Converting: file.pkl -> file.json")
json_obj = json.loads(json.dumps(pickle_obj, default=str))

# write the json file
print ("...Writing file.json")
with open(
        os.path.splitext(sys.argv[1])[0] + '.json',
        'w',
        encoding='utf-8'
    ) as outfile:
    json.dump(json_obj, outfile, ensure_ascii=False, indent=4)

print ("...Done")