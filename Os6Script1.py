#!/usr/bin/env python
#script creates 1000 VLANS (2-1002), then verifies 1000 were created
import sys, telnetlib, re
#variable declaration
#Replace the “xx.xx.xx.xx” below with the local host’s IP address
hostname = '10.81.13.30'
username = 'admin'
password = 'WalkingRoute##'
enaPassword = 'WalkingRoute##'
enPrompt = '>'
confPrompt = '#'
#open a telnet session to the device
print ("Opening telnet session to the device")
# t = telnetlib.Telnet(hostname)
expect = t.read_until
send = t.write
expect('login as:')
send(username + '\r')
expect('Password:')
send(password + '\r')
expect(enPrompt)
send('enable\r')
expect('Password:')
send(enaPassword + '\r')
expect(confPrompt)
send('terminal length 0\r')
expect(confPrompt)
send('configure terminal\r')
expect(confPrompt)
#loop to create vlans
    # print("Creating 1000 VLANs on the switch")
    # for x in range(2, 1002):
    # cmd = "vlan %d" % (x)
    # send(cmd + '\r')
    # expect(confPrompt)
    # send('exit\r')
    # expect(confPrompt)

    # #parse to count vlans created
    # print("Verifying the VLAN database")
    # send('show vlan\r')
    # vlan = expect(confPrompt)
    # totalVlan = re.findall(r"VLAN(\d+){3}", vlan)
    # exp = len(range(2, 1002))
    # #if-else to determine output
    # if len(totalVlan) == exp:
    # print(exp, ("VLANs are created on the switch"))
    # else:
    # print("Failed to create required number of VLANs on the switch")
#close the telnet session
print ("Closing the telnet session")
# t.close()
