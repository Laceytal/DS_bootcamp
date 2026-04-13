#!/usr/bin/env python3
import os

venv = os.environ.get("VIRTUAL_ENV")
if venv:
    print(f"Your current virtual env is {venv}")
else:
    print("No virtual environment is currently active.")
