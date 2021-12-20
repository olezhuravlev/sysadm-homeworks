#!/usr/bin/env python3

import json
import pathlib
import socket

import yaml

# Mark for IP that not obtained.
no_ip = "UNKNOWN"

# Filename to store data to.
json_filename = 'data.json'
yaml_filename = 'data.yaml'

# Hosts to check.
hosts = ["drive.google.com", "mail.google.com", "google.com", "asdfgadsf.com"]

# Examine hosts for their ip and store values in a set
hosts_ips_current = dict()
for host in hosts:

    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        ip = no_ip

    hosts_ips_current[host] = ip

# After data obtained show it to user.
for key in hosts_ips_current:
    print("{host}-{ip}".format(host=key, ip=hosts_ips_current[key]))

# Get previously stored IPs for the hosts (if any).
if pathlib.Path(json_filename).is_file():
    with open(json_filename, 'r') as f:
        hosts_ips_old = json.load(f)

    # Check if IPs of the services has been changed
    hosts_ips_diff = dict()
    for key in hosts_ips_current:
        if hosts_ips_current[key] != hosts_ips_old[key]:
            hosts_ips_diff[key] = (hosts_ips_old[key], hosts_ips_current[key])

    # Inform user about changed IPs:
    for key in hosts_ips_diff:
        ips = hosts_ips_diff[key]
        print("[ERROR]{host} IP mismatch: {old} {new}".format(host=key, old=ips[0], new=ips[1]))

# Store obtained data to a JSON-file in user-friendly format.
hosts_ips_json = json.dumps(hosts_ips_current, indent=2, sort_keys=False)
with open(json_filename, 'w', encoding='utf-8') as f:
    f.write(hosts_ips_json)

# Store obtained data to a YAML-file in user-friendly format.
hosts_ips_yaml = yaml.dump(hosts_ips_current, explicit_start=True, explicit_end=True, sort_keys=False)
with open(yaml_filename, 'w', encoding='utf-8') as f:
    f.write(hosts_ips_yaml)
