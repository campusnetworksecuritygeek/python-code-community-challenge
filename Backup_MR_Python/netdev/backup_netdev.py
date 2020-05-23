# By morad rachad
import asyncio
import netdev
import datetime
import os
import time
import data_netdev

print ('############################# NETDEV LIBRARY #############################\n')
print ('############################### '+ str((datetime.datetime.now()).date()) +' ###############################\n')

async def task(devices):
    for param in devices:
        # The main folder it should be already created 
        os.chdir('E:\Backup')
        backupDirName = str((datetime.datetime.now()).date())
        x = os.path.isdir(backupDirName)
        # Script will create a folder هn the name of today's date & if the folder already exist will skip this line        
        if x == False:
            os.mkdir(backupDirName)
        os.chdir(backupDirName)
        # inside the folder that was created befor it will be create another folder with name of device & if the folder already exist will skip this line        
        z = os.path.isdir(param[1])
        if z == False:
            os.mkdir(param[1])
        os.chdir(param[1])
        # inside the device folder it will be create a file with name "running-config.cfg" & if the file already exist Will be erased the old backup with the new backup 
        f = open("E:\Backup/"+ backupDirName +"/"+ param[1] +"/running-config.cfg", "a")
        # Connect with the device        
        async with netdev.create(**param[0]) as ios:
            # moment of start process with this device        
            start_time = time.time()
            print ('+++ Getting the backup from Switch " '+ str(param[1]) +' " :')
            # the script will send this 2 command into the device         
            await ios.send_command("terminal length 1000")
            output = await ios.send_command("show run")
            # save the run config into the file that was created for this device            
            print(output, file=f)
            print ("\t--- %.2f seconds. " % (time.time() - start_time))
            print ('\t--- The backup has been successfully completed. \n')
            # moment of end process with this device

async def run():
    start_time = time.time()
    # import devices information from file " data_netdev.py "    
    devices = [data_netdev.Sw0, data_netdev.Sw1, data_netdev.Sw2, data_netdev.Sw3, data_netdev.Sw4]
    tasks = [task(devices)]
    # run the function " task "
    await asyncio.wait(tasks)
    print ("\n\n+++ All the process token %.2f seconds. \n" % (time.time() - start_time))
    input("- Press ENTER to EXIT !!!")
    # moment of end the script

# run the function " run "
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
