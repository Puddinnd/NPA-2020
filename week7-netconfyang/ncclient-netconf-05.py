from ncclient import manager
import xmltodict

m = manager.connect(
    host = "10.0.15.178",
    port = 830,
    username = "cisco",
    password = "cisco!123",
    hostkey_verify = False
)

netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
            <name>1</name>
            <description>example loopback</description>
            <ip>
                <address>
                    <primary>
                    <address>10.1.100.1</address>
                    <mask>255.255.255.0</mask>
                    </primary>
                </address>
            </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_loopback)
data_json = xmltodict.parse(str(netconf_reply))
print(data_json)
