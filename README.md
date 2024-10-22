# JetbrainsLock
Delete lock files that forbid to open Jetbrains IDE
# Utility for removing JetBrains lock files

This small utility written in Python is designed to remove lock files (.lock) created by some JetBrains products in Linux (e.g. Ubuntu) that can cause errors when running applications.

## Usage

1. **Copy the script:** Save the Python code above as the `delete_lock.py` file.
2. **Replace `your_username`:** Change the file paths in the script, replacing `your_username` with your Linux username.
3. **Run the script:** Open a terminal and run the command `python3 delete_lock.py`.

## Note

* Make sure the lock file paths in the script match your configuration. 
* If the default paths are correct, you do not need to change anything.
* The script will check the existence of each file before deleting it and display a message.
