import json

config = json.load(open("config/serviceConfig.json"))
# load info from json!
print(config.get('mpr'))

