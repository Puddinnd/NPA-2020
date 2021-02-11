from netmiko import ConnectHandler

device_ip = "172.31.178.1"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}

with ConnectHandler(**device_params) as ssh:
    result = ssh.send_command('sh ip int br')
    print(result)
