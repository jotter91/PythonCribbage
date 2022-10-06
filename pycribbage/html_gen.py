import json 

def load_json(fname):
    with open(fname) as json_file:
        data = json.load(json_file)
    return data

def update_template():
    pass
