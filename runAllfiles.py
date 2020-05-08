import subprocess
import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".c"):
            subprocess.call(["gcc", os.path.join(root, file)])
            subprocess.call(["./a.out"])

for root, dirs, files in os.walk("pythonfiles"):
    for file in files:
        if file.endswith(".py"):
            subprocess.call(["python", os.path.join(root, file)])