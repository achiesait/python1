from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
secret = getpass("Enter secret: ")

dell1330 = {
    "device_type": "dell_os6",
    "host": "10.81.13.30",
    "username": "admin",
    "password": password,
    "secret": secret,
}

net_connect = ConnectHandler(**dell1330)
# Call 'enable()' method to elevate privileges
net_connect.enable()
print(net_connect.find_prompt())
net_connect.disconnect()
