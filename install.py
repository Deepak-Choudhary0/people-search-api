import os

os.system('sudo apt update')
os.system('sudo apt upgrade')
os.system('sudo apt install sqlite3')
os.system('sudo apt update')
os.system('sudo apt upgrade')

command = f'echo "Successfully Installed the required Dependencies for Deepak project People-Search-Api !"'
os.system(command)