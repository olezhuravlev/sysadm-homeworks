#!/usr/bin/env python3
import os

dir_to_check = "~/DevOps/sysadm-homeworks"
bash_command = ["cd " + dir_to_check, "git status"]
sys_command = ' && '.join(bash_command)
result_os = os.popen(sys_command).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(dir_to_check + "/" + prepare_result)
