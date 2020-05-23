# Using Netmiko & Netdev for getting Backup.

These example scripts use the Netmiko & Netdev Python library to backup with a device through CLI

If you don't know what is netmiko or netdev check these two link :
	- [Netmiko library](https://pypi.org/project/netmiko/)
	- [Netdev library](https://pypi.org/project/netdev/)

These Python scripts leverages Netmiko & Netdev to:
  - Create folder with name of this day
  - Inside the folder that was created befor, script will create folder with the name of any device in your lab.
  - Inside the folder of the device, script will do a backup for the device with name "running_config.cfg"

This script has been tested with Python 3.7.0, however may work with other versions.  

## Requirements

Python

- netmiko
- netdev
- asyncio

# Getting Started
* Clone the Python Examples and change into the directory.  

    ```bash
    git clone //github.com/campusnetworksecuritygeek/python-code-community-challenge/tree/master/Backup_MR_Python
    cd Backup_MR_Python
    ```

* Install the requirements

    ```bash
    pip3 install netmiko
    pip3 install netdev
    pip3 install asyncio
    ```

* 1- Testing Netmiko scripts :
    ```
		# cd Backup_MR_Python/Netmiko/
    # Run the backup script 
    $ python backup_netmiko.py

    # Output :  
		############################# NETMIKO LIBRARY ############################
		############################### 2020-05-23 ###############################

		+++ Getting the backup from Switch " RDC " :
						--- 3.78 seconds.
						--- The backup has been successfully completed.

		+++ Getting the backup from Switch " Etage_1 " :
						--- 3.78 seconds.
						--- The backup has been successfully completed.

		+++ Getting the backup from Switch " Etage_2 " :
						--- 3.78 seconds.
						--- The backup has been successfully completed.

		+++ Getting the backup from Switch " Etage_3 " :
						--- 3.78 seconds.
						--- The backup has been successfully completed.

		+++ Getting the backup from Switch " Etage_4 " :
						--- 3.77 seconds.
						--- The backup has been successfully completed.

		+++ All the process token 43.39 seconds.

		- Press ENTER to EXIT !!!
		```

* 2- Testing Netdev scripts :
    ```
		# cd Backup_MR_Python/Netmiko/
    # Run the backup script 
    $ python backup_netmiko.py

    # Output :  
		############################# NETDEV LIBRARY #############################
		############################### 2020-05-23 ###############################

		+++ Getting the backup from Switch " RDC " :
						--- 0.14 seconds.
						--- The backup has been successfully completed.

		+++ Getting the backup from Switch " Etage_1 " :
						--- 0.16 seconds.
						--- The backup has been successfully completed.

		+++ Getting the backup from Switch " Etage_2 " :
						--- 0.16 seconds.
						--- The backup has been successfully completed.

		+++ Getting the backup from Switch " Etage_3 " :
						--- 0.14 seconds.
						--- The backup has been successfully completed.

		+++ Getting the backup from Switch " Etage_4 " :
						--- 0.15 seconds.
						--- The backup has been successfully completed.

		+++ All the process token 3.60 seconds.

		- Press ENTER to EXIT !!!
		```

* 3- Resulta in the folder E:/Backup :
    ```
		PC@RACHAD MINGW64 /E/Backup
		$ pwd
		/E/Backup

		PC@RACHAD MINGW64 /e/Backup
		$ ll
		total 0
		drwxr-xr-x 1 PC 197121 0 mai   23 02:58 2020-05-23/

		PC@RACHAD MINGW64 /E/Backup
		$ ll
		total 0
		drwxr-xr-x 1 PC 197121 0 mai   23 02:58 2020-05-23/

		PC@RACHAD MINGW64 /E/Backup
		$ cd 2020-05-23/
		Etage_1/ Etage_2/ Etage_3/ Etage_4/ RDC/

		PC@RACHAD MINGW64 /E/Backup
		$ cd 2020-05-23/Etage_1

		PC@RACHAD MINGW64 /E/Backup/2020-05-23/Etage_1
		$ ll
		total 12
		-rw-r--r-- 1 PC 197121 8458 mai   23 18:11 running-config.cfg
		 ```

		
