#!/usr/bin/env python3
import pathlib
import sys
from subprocess import Popen, PIPE

# If directory is not specified via CLI-parameter then directory of the script is used to check.
dir_to_check = str(pathlib.Path(__file__).parent.resolve())
if len(sys.argv) > 1:
    dir_to_check = sys.argv[1]

# Invoke system command with access to standard streams.
bash_command = ["cd " + dir_to_check, "git status"]
proc = Popen(' && '.join(bash_command), shell=True, stdout=PIPE, stderr=PIPE)
stdout, stderr = proc.communicate()

# Check if there are any errors (including 'not a git repository').
stderr_decoded = stderr.decode('utf-8')
if stderr_decoded:
    print("Error for directory " + dir_to_check + ": " + stderr_decoded)
    exit(1)

# Get result of "git status" command.
stdout_decoded = stdout.decode('utf-8')
is_change = False
for result in stdout_decoded.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(dir_to_check + "/" + prepare_result)
        is_change = True

# If there were no modified files then inform the user.
if not is_change:
    print("No modified files in directory: " + dir_to_check)
