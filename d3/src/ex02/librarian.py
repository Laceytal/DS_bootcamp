#!/usr/bin/env python3
import os
import sys
import subprocess

def main():
    venv = os.environ.get("VIRTUAL_ENV")
    if not venv:
        raise EnvironmentError("Not inside a virtual environment!")
    if not venv.endswith("edgar"): 
        raise EnvironmentError("You are in the wrong virtual environment!")
    with open("requirements.txt", "w") as f:
        f.write("beautifulsoup4\n")
        f.write("pytest\n")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
    with open("requirements.txt", "w") as f:
        f.write(result.stdout)

    print(result.stdout.strip())

if __name__ == "__main__":
    main()
