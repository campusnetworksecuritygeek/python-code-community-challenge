# By morad rachad
from netmiko import ConnectHandler
import datetime
import os
import time
import data_netmiko

# import devices information from file " data_netmiko.py "
SW_BASE = [data_netmiko.Sw0, data_netmiko.Sw1, data_netmiko.Sw2, data_netmiko.Sw3, data_netmiko.Sw4]
# A moment of start script
start_time = time.time()

print ('############################# NETMIKO LIBRARY ############################\n')
print ('############################### '+ str((datetime.datetime.now()).date()) +' ###############################\n')
def connectToDevice(SW_BASE):
    for SW in SW_BASE :
        # The main folder it should be already created 
        l = os.chdir('E:\Backup')
        backupDirName = str((datetime.datetime.now()).date())
        x = os.path.isdir(backupDirName)
        # Script will create a folder هn the name of today's date & if the folder already exist will skip this line
        if x == False:
            os.mkdir(backupDirName)
        os.chdir(backupDirName)
        # inside the folder that was created befor it will be create another folder with name of device & if the folder already exist will skip this line
        z = os.path.isdir(SW[1])
        if z == False:
            os.mkdir(SW[1])
        os.chdir(SW[1])
        # inside the device folder it will be create a file with name "running-config.cfg" & if the file already exist Will be erased the old backup with the new backup
        f = open("E:\Backup/"+ backupDirName +"/"+ SW[1] +"/running-config.cfg", "a")
        # Connect with the device
        net_connect = ConnectHandler(**SW[0])
        # moment of start process with this device
        start_time = time.time()
        print ('+++ Getting the backup from Switch " '+ str(SW[1]) +' " :')
        # the script will send this 2 command into the device
        net_connect.send_config_set('terminal length 1000')
        output = net_connect.send_command('show run')
        # deconnect with the device
        net_connect.disconnect()
        # save the run config into the file that was created for this device
        print(output, file=f)
        print ("\t--- %.2f seconds. " % (time.time() - start_time))
        print ('\t--- The backup has been successfully completed. \n')
        # moment of end process with this device

# run the function
connectToDevice(SW_BASE)

# moment of end the script
print ("\n\n+++ All the process token %.2f seconds. \n" % (time.time() - start_time))
input("- Press ENTER to EXIT !!!")
