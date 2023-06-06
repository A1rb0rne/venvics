import sys
import os

def is_virtual_env():
    return sys.prefix != sys.base_prefix

if is_virtual_env():
    print(f"You are in a virtual environment at {sys.prefix}")
else:
    print("You are not in a virtual environment")
