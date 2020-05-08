import sys

print("Add is executing")
if len(sys.argv) == 3:
    print(f"Param #1: {sys.argv[1]}")
    print(f"Param #1: {sys.argv[2]}")
    print(int(sys.argv[1])+int(sys.argv[2]))