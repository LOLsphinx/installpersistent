import os
import time

def command(commands):
	os.system(commands)

def clear():
	os.system("clear")

def sleep(secs):
	time.sleep(secs)

osname = os.name()

if osname == "posix":
	pass
elif osname == "nt":
	exit()
else:

	print("Unknown System name.")
	time.sleep(2.4)
	clear()


clear()

os.system("sudo fdisk -l | grep 'devices'")

print()
print('', end="", flush=True)
for _ in range(3):
	print(".", end="", flush=True)


print()
print("Please select your USB Device that linux live OS has installed.")
print()
device = input("Type the Device: ")
time.sleep(2.4)
clear()
print("Please name your system directory: ")
print("Example: (my_usb, mysystem). - This is OPTIONAL -")
systemdir = input("Name of your System Folder: ")

if not systemdir:
	try:
		print()
		print("You didn't name your system.")
		sleep(1.4)
		print("We're naming it in default (my_usb).")
		command("sudo mkdir -p /mnt/my_usb")
		sleep(1)
		command(f"sudo mount /dev/{device} /mnt/my_usb")
		sleep(1)
		command(f"sudo umount /dev/{device}")
		clear()
		print("Persistent has been installed properly")
		sleep(3.5)
		clear()
		dirdesk = "~/Desktop"
		if os.path.exists(dirdesk):
			command("touch ~/Desktop/LetsTestThePersistent.txt")
			command("echo Let's try to test the persistent let's see if this text will be still here once you restart your pc. >> ~/Desktop/LetsTestThePersistent.txt")
			print("Please check the txt in your Desktop. and Read it. Thankyou!")
		else:
			clear()
			print("LetsTestThePersistent.txt not exists!")
			sleep(3.1)
			exit()
	except Exception as e:
		clear()
		print("There was an error on installing")
		print(e)
		exit()
elif len(systemdir) <= 2:
	clear()
	print("You input a length of 2 chars!!")
	print("kindly input greater or equals to 3 Chars. Thankyou!")
	sleep(2.7)
	exit()
elif '/' in systemdir:
    clear()
    print("Input contains '/', please remove the '/'.")
    print("Please Redo.")
    exit()
elif '/' in device:
    clear()
    print("In user input usb device contains '/', please remove the '/'.")
    print("Please Redo.")
    exit()
else:
	try:
		print()
		print(f"Renaming with {systemdir}.")
		sleep(1.4)
		command(f"sudo mkdir -p /mnt/{systemdir}")
		sleep(1)
		command(f"sudo mount /dev/{device} /mnt/{systemdir}")
		sleep(1)
		command(f"sudo umount /dev/{device}")
		clear()
		print("Persistent has been installed properly")
		sleep(3.5)
		clear()
		dirdesk = "~/Desktop"
		if os.path.exists(dirdesk):
			command("touch ~/Desktop/LetsTestThePersistent.txt")
			command("echo Let's try to test the persistent let's see if this text will be still here once you restart your pc. >> ~/Desktop/LetsTestThePersistent.txt")
			print("Please check the txt in your Desktop. and Read it. Thankyou!")
		else:
			clear()
			print("LetsTestThePersistent.txt not exists!")
			sleep(3.1)
			exit()
	except Exception as e:
		clear()
		print("There was an error on installing")
		print(e)
		exit()
