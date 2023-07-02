import json

global default
f = open("config.json")
default = json.load(f)

