#show_cisco_int_pmk.py

import paramiko

host='10.81.13.30'

port=22

username='admin'

password='admin'

#cisco ios command to get a list of vlans

cmd= 'show vlan \n'

def main():

    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, port, username, password)

        stdin, stdout, stderr = ssh.exec_command(cmd)

        output_lines = stdout.readlines()

        response = ''.join(output_lines)

        print(response)

    finally:

        ssh.close()

    if __name__ == '__main__':

main()




def write_descr(ip, username, password, enable_secret, localint, descr):
    ssh_connection = ConnectHandler(
        device_type = 'cisco_ios',
        ip = ip,
        username = username,
        password = password,
        secret = enable_secret
    )
    ssh_connection.enable()
    rt = ssh_connection.find_prompt() + "\n"
    rt = ssh_connection.send_command("conf t", delay_factor=0)
    rt = ssh_connection.send_command("int "+localint, delay_factor=0)
    rt = ssh_connection.send_command("description "+descr, delay_factor=0)
    ssh_connection.disconnect()





    def push_config_commands(username, password, ip_address, vendor_class, secret, commands):
    try:
        net_connect = ConnectHandler(device_type=vendor_class, ip=ip_address, username=username, password=password, secret=secret)
        net_connect.enable()
        output = net_connect.send_config_set(commands)
        print output
    except:
        print 'Error in either connecting or executing configuration command @ ' + ip_address





from netmiko import ConnectHandler
import socket


class NetOperator(object):
    def __init__(self):
        self.username = "python"
        self.password = "*"

device_type = "cisco_ios"

current_operator = NetOperator()


def show_version(current_device):

    device_ip = socket.gethostbyname(current_device)
    command = "show version"
    net_connect = ConnectHandler(
            device_type=device_type,
            ip=device_ip,
            username=current_operator.username,
            password=current_operator.password
    )

    net_connect.find_prompt()
    net_connect.enable()
    output = net_connect.send_command(command)

    return (output)