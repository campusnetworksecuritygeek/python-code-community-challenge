#SAMPLE CODE TO BACKUP CONFIGURATION OF CISCO DEVICE
#BY EL HASSAN EL AMRI

from netmiko import ConnectHandler
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
import io

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.17.154',
    'username': 'user',
    'password': 'pass',
}


net_connect = ConnectHandler(**cisco_device)
output_host = net_connect.send_command('sh run | i host')
output_run  = net_connect.send_command('sh run')
f = io.open("/home/backup/device-" + output_host.split()[1] + "-" + timestr, 'w', encoding='utf8')
f.write(output_run)
