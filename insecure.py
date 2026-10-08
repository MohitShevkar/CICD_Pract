import subprocess

command = input("Enter a command: ")

subprocess.call(command, shell=True)