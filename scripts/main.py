# Importing needed packages
import os
import glob
import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

# Displaying PowerBash logo
print("""
██████╗░░█████╗░░██╗░░░░░░░██╗███████╗██████╗░██████╗░░█████╗░░██████╗██╗░░██╗
██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░██║
██████╔╝██║░░██║░╚██╗████╗██╔╝█████╗░░██████╔╝██████╦╝███████║╚█████╗░███████║
██╔═══╝░██║░░██║░░████╔═████║░██╔══╝░░██╔══██╗██╔══██╗██╔══██║░╚═══██╗██╔══██║
██║░░░░░╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║██████╦╝██║░░██║██████╔╝██║░░██║
╚═╝░░░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
""")


# Defining 'run_command()' function and make it run commands
def run_command():
    # 'exit' command
    if command == "exit":
        exit()
    # 'hostname' command
    elif command == "hostname":
        print(host_name)
    # 'hostip' command
    elif command == "hostip":
        print(host_ip)
    # 'ls' command
    elif command == "ls":
        path = input("Enter the path to list the folders and files in: ")
        if not path.endswith('/'):
            path = f'{path}/'
        folders = glob.glob(f'{path}*/')
        for folder in folders:
            print(folder[len(path):])
        for file in glob.glob(f'{path}*'):
            if os.path.isfile(file):
                print(file[len(path):])
    # 'cp' or 'copy' command
    elif command == "cp" or command == "copy":
        original_path = input("Enter the path of the file you want to copy: ")
        copy_to = input("Enter the path where you want to copy it to: ")
        os.system(f'cp {original_path} {copy_to}')
    # 'mv' or 'move' command
    elif command == "mv" or command == "move":
        original_path = input("Enter the path of the file you want to move: ")
        move_to = input("Enter the path where you want to move it to: ")
        os.system(f'mv {original_path} {move_to}')
    # Error message when command not found
    else:
        print(f"Sorry, the command \"{command}\" is not recognised as a command!")


# Allowing the users to run commands
while True:
    command = input(">>> ")
    run_command()
