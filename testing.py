from contextlib import ContextDecorator
import json

name = "sheesh"
email = "ss@email.com"
contact = {name: email}
data = json.load(open('db.json'))
if type(data) is dict:
    data = [data]
# append new item to data lit
data["contacts"].append({name: email})
with open('db.json', 'w') as json_file:
    json.dump(data, json_file)