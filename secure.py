import subprocess

command = ["cmd.exe", "/c", "echo", "Hello from secure application"]

subprocess.run(command, check=True)