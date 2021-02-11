from netmiko import ConnectHandler

y = 178
x = 8

def setIPtoInterface(device_params, interface, ip, subnet):
    with ConnectHandler(**device_params) as ssh:
        ssh.config_mode()
        commands = [
            "int {}".format(interface),
            "ip add {} {}".format(ip, subnet),
            "no shut",
        ]
        ssh.send_config_set(commands)
        ssh.exit_config_mode()
        ssh.send_command('write mem')
        result = ssh.send_command('sh ip int br')
        ssh.disconnect()
        return result

def main():
    device_ip = "172.31.178.1"
    username = "admin"
    password = "cisco"

    device_params = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": username,
        "password": password,
    }
    result = setIPtoInterface(device_params, "lo0", "172.20.178.1", "255.255.255.255")
    print(result)

    
main()
