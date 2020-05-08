import subprocess

subprocess.call(["g++", "hello_world.cpp"])
tmp=subprocess.call("./a.out")
print ("printing result")
print(tmp)