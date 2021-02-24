from ncclient import manager
import xmltodict

m = manager.connect(
    host = "10.0.15.178",
    port = 830,
    username = "cisco",
    password = "cisco!123",
    hostkey_verify = False
)

netconf_hostname = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <hostname>R178-NEW</hostname>
 </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname)
data_json = xmltodict.parse(str(netconf_reply))
print(data_json)
