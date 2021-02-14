from netmiko import ConnectHandler
from pprint import PrettyPrinter
from Utils import *
import yaml

pp = PrettyPrinter(indent=2)
config_path = "./config/"

def convertData(data):
    replace_list = [
        ["administratively down", "down"],
        ["GigabitEthernet", "g"],
        ["FastEthernet", "f"],
        ["Loopback", "lo"]
    ]
    for w in replace_list:
        data = data.replace(w[0], w[1])
    data = data.split()
    data = [data[i:i+6] for i in range(0, len(data), 6)]
    dict_data = {}
    for i in data[1:]:
        dict_data[i[0]] = i[1:]
    return dict_data

def verifyDeviceInfo(device):
    status = True
    device_ip = device["management_ip"]
    device_params = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": username,
        "password": password,
    }
    with ConnectHandler(**device_params) as ssh:
        interfaces_data = convertData(ssh.send_command('sh ip int br')) 
        # print(interfaces_data)
        # print(device)
        if device["name"][0] == 'R' and device["management_ip"] != interfaces_data["g0/0"][0]:
            return False
        elif device["name"][0] == 'S' and device["management_ip"] != interfaces_data["Vlan99"][0]:
            return False
        if type(device['interfaces']) is list:
            for d in device['interfaces']:
                if d["ip"] != interfaces_data[d["name"]][0]:
                    # print(d)
                    # print(interfaces_data[d["name"]])
                    delay_print("[*] Configuring: {} inteface {}".format(device['name'], d['name']), False)
                    setIPtoInterface(device_params, d['name'], d['ip'], d['subnet'])
                    status = False
    return status

def main():
    devices_config = yaml.load(open(config_path + "devices_interface_info.yml"), Loader=yaml.Loader)
    # pp.pprint(devices_config)
    for device in devices_config:
        delay_print("[*] Verifying: " + device['name'], False)
        status = verifyDeviceInfo(device)
        if status:
            delay_print("[+] "+device['name'] + " status: [OK]                  ", True)
        else:
            delay_print("[-] "+device['name'] + " status: [Fixed]               ", True)
        # break

main()
