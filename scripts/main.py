import os
import glob


def run_command():
    if command == "exit":
        exit()
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
    else:
        print(f"Sorry, the command \"{command}\" is not recognised as a command!")


while True:
    command = input(">>> ")
    run_command()
