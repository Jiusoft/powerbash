# Importing Libraries we need for this Terminal
import os
import socket
import glob

# Defining the Hostname and HostIP
hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)

# Displaying the label
print("""
░░░░░██╗██╗██╗░░░██╗████████╗███████╗██████╗░███╗░░░███╗
░░░░░██║██║██║░░░██║╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░░░██║██║██║░░░██║░░░██║░░░█████╗░░██████╔╝██╔████╔██║
██╗░░██║██║██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║
╚█████╔╝██║╚██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░╚════╝░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
""")

# Running the main process
while True:
    command = input(">>> ")

    if command == 'ping':
        website = input("Enter the website to ping: ")
        os.system('ping ' + website)

    if command == 'cp':
        originalfile = input("Enter where your original file is: ")
        copytofolder = input("Enter where you want to copy it: ")
        os.system('copy ' + originalfile + ' ' + copytofolder)

    if command == 'mv':
        originallocation = input("Enter where your file is: ")
        distfolder = input("Enter where you want to move it: ")
        os.system('move ' + originallocation + ' ' + distfolder)

    if command == 'ren':
        path = input("Enter the path where the file you want to rename is located: ")
        originalname = input("Enter the original file name: ")
        distname = input("Enter the new file name: ")
        os.system('cd ' + path + ' && ren ' + originalname + ' ' + distname)
        print("File renamed!")

    if command == 'runcmdinterminal':
        cmdinterminal = input("Enter the command you want to run in terminal: ")
        os.system(cmdinterminal)

    if command == 'hostname':
        print(hostname)

    if command == 'hostip':
        print(hostip)

    if command == 'ls':
        path = input("Enter the path you want to list the files and folders: ")
        addslash = path.endswith('/')
        if addslash == True:
            print(glob.glob(path + "*"))
        if addslash == False:
            print(glob.glob(path + "/*"))
