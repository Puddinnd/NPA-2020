from ncclient import manager
import xmltodict

m = manager.connect(
    host = "10.0.15.178",
    port = 830,
    username = "cisco",
    password = "cisco!123",
    hostkey_verify = False
)

netconf_delete_loopback = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
            <name>Loopback1</name>
        </interface>
    </interfaces>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_delete_loopback)
data_json = xmltodict.parse(str(netconf_reply))
print(data_json)
