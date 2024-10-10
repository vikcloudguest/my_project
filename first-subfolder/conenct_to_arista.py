import re
test = "On Friday, I will study Python for Network Automation."
x = re.findall('on', test)
print(x)

test = " I will study Python for Network Automation." # till the first match
x = re.search('on', test)
print(x)
print(x.start())

test = "Network Automation."
x = re.split('o', test)
print(x)

test = "Network Automation."
x = re.split('o', test, 1)
print(x)

test = "Network Automation."
x = re.sub('o', 'XXX', test, )
print(x)
test = "Network Automation."
x = re.sub('o', 'XXX', test, 2)
print(x)

# test = "You can learn Python Scripting in 10 Weeks."
# print(re.findall('S\w',test))
#
# test = "You can learn Python Scripting in 10 Weeks."
# print(re.findall('S\D+',test))
#
# test = "You can learn Python Scripting in 10 Weeks."
# print(re.findall('S(\w+)',test))


from netmiko import ConnectHandler
from getpass import getpass

device_list = ['10.1.1.1', '10.2.2.2']
for ip in device_list:
    device1 = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "pyclass",
        "password": 'Testin!ng',
    }
    print(device1)