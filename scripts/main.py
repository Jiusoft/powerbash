# Importing needed packages
import os
import glob

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
    # Error message when command not found
    else:
        print(f"Sorry, the command \"{command}\" is not recognised as a command!")


# Allowing the users to run commands
while True:
    command = input(">>> ")
    run_command()
