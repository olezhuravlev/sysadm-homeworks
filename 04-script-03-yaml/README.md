# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательные задания

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
	```json
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
	```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

Здесь три ошибки:

* IP-адрес должен возвращаться в виде строки, потому что это не число;
* не хватает закрывающей кавычки в ноде `"ip"` последнего элемента;
* по-видимому, сервер возвращает некорректный IP для первого элемента.

````json
 {
  "info": "Sample JSON output from our service\t",
  "elements": [
    {
      "name": "first",
      "type": "server",
      "ip": "71.75.XXX.XXX"
    },
    {
      "name": "second",
      "type": "proxy",
      "ip": "71.78.22.43"
    }
  ]
}
````

---

2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному
   функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по
   одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в
   момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Скрипт:

````python
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
````

#### Вывод скрипта при запуске при тестировании:

````bash
./2.py
drive.google.com-64.233.162.194
mail.google.com-74.125.131.18
google.com-74.125.131.139
asdfgadsf.com-UNKNOWN
[ERROR]mail.google.com IP mismatch: 74.125.131.17 74.125.131.18
[ERROR]google.com IP mismatch: 74.125.131.101 74.125.131.139

Process finished with exit code 0
````
Как и в предыдущем варианте этой задачи видим, что IP-адреса сервисов `mail.google.com` и `google.com` успели измениться.
#### json-файл, который записал скрипт:

````json
{
  "drive.google.com": "64.233.162.194",
  "mail.google.com": "74.125.131.18",
  "google.com": "74.125.131.139",
  "asdfgadsf.com": "UNKNOWN"
}
````

#### yml-файл, который записал скрипт:

````yaml
---
drive.google.com: 64.233.162.194
mail.google.com: 74.125.131.18
google.com: 74.125.131.139
asdfgadsf.com: UNKNOWN
...
````

Все созданные файлы приложены к решению.

---