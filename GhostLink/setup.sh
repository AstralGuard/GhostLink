#!/bin/bash

echo "[+] Initializing GhostLink Environment..."

if ! command -v python3 &> /dev/null
then
    echo "[!] Python3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "[✓] Python3 detected:"
python3 --version

echo "[✓] No external dependencies required."
echo "[✓] Environment ready."
echo "[✓] You can now run: python3 ghostlink.py"
