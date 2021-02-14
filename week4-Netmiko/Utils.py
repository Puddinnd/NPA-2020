import io
import sys
import time

username = "admin"
password = "cisco"

def backline():
    print('\r', end='')

def delay_print(s, newline):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    if newline:
        print()
    else:
        backline()

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
        ssh.save_config()
        result = ssh.send_command('sh ip int br')
        ssh.disconnect()
        return result