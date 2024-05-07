import os
import time
import subprocess

osname = os.name

def command(commands):
    subprocess.run(commands, shell=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def sleep(secs):
    time.sleep(secs)

if osname == "posix":
    pass
elif osname == "nt":
    exit()
else:
    print("Unknown System name.")
    time.sleep(2.4)
    clear()
    exit()

clear()

command("sudo fdisk -l | grep 'devices'")

print()
print('', end="", flush=True)
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)

print("\nPlease select your USB Device that the Linux live OS has installed.")
print("Example: sdb")
device = input("Type the Device Path: ")
time.sleep(2.4)
clear()

print("Please name your system directory (OPTIONAL): ")
print("Example: my_usb, mysystem")
systemdir = input("Name of your System Folder: ")

if not systemdir:
    try:
        print()
        print("You didn't name your system.")
        sleep(1.4)
        print("We're naming it in default (my_usb).")
        command("sudo mkdir -p /mnt/my_usb")
        sleep(1)
        command(f"sudo mount {device} /mnt/my_usb")
        sleep(1)
        command(f"sudo umount {device}")
        clear()
        print("Persistent has been installed properly")
        sleep(3.5)
        clear()
        dirdesk = os.path.expanduser("~/Desktop")
        if os.path.exists(dirdesk):
            command("touch ~/Desktop/LetsTestThePersistent.txt")
            command("echo 'Let\'s try to test the persistent let\'s see if this text will still be here once you restart your PC.' >> ~/Desktop/LetsTestThePersistent.txt")
            print("Please check the txt file on your Desktop and read it. Thank you!")
        else:
            clear()
            print("Desktop does not exist!")
            print("Let's try to create a LetsTestThePersistent.txt on the current Directory!")
            command("echo 'Let\'s try to test the persistent let\'s see if this text will still be here once you restart your PC.' > LetsTestThePersistent.txt")
            print("Please kindly read what's in the Text file 'LetsTestThePersistent.txt'. ")
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
    print("Kindly input greater or equals to 3 chars. Thank you!")
    sleep(2.7)
    exit()
elif '/' in systemdir:
    clear()
    print("Input contains '/', please remove the '/'.")
    print("Please redo.")
    exit()
elif '/' in device:
    clear()
    print("User input for USB device contains '/', please remove the '/'.")
    print("Please redo.")
    exit()
else:
    try:
        print()
        print(f"Renaming with {systemdir}.")
        sleep(1.4)
        command(f"sudo mkdir -p /mnt/{systemdir}")
        sleep(1)
        command(f"sudo mount {device} /mnt/{systemdir}")
        sleep(1)
        command(f"sudo umount {device}")
        clear()
        print("Persistent has been installed properly")
        sleep(3.5)
        clear()
        dirdesk = os.path.expanduser("~/Desktop")
        if os.path.exists(dirdesk):
            command("touch ~/Desktop/LetsTestThePersistent.txt")
            command("echo 'Let\'s try to test the persistent let\'s see if this text will still be here once you restart your PC.' >> ~/Desktop/LetsTestThePersistent.txt")
            print("Please check the txt file on your Desktop and read it. Thank you!")
        else:
            clear()
            print("LetsTestThePersistent.txt does not exist on Desktop!")
            sleep(3.1)
            exit()
    except Exception as e:
        clear()
        print("There was an error on installing")
        print(e)
        exit()
