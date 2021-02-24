from ncclient import manager
from pprint import pprint
import xmltodict
import json

m = manager.connect(
    host = "10.0.15.178",
    port = 830,
    username = "cisco",
    password = "cisco!123",
    hostkey_verify = False
)

netconf_reply = m.get_config(source="running")
# print(netconf_reply)

### Export data from XML to JSON file.
data_json = xmltodict.parse(str(netconf_reply))
f = open("data-01.json", "w+")
json.dump(data_json, f ,indent=2)