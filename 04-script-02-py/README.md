# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательные задания

1. Есть скрипт:

````python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
````

| Вопрос                                       | Ответ                                                                                                                                                                                                      |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Какое значение будет присвоено переменной c? | Никакого - операция суммирования `<int>` и `<str>` не поддерживается. Автоматического преобразования типов не происходит, потому что неизвестно, какой именно из участвующих типов требуется в результате. |
| Как получить для переменной c значение 12?   | Требуется явное преобразование `<int>` в `<str>`:<br/>c = str(a) + b                                                                                                                                       |
| Как получить для переменной c значение 3?    | Требуется явное преобразование `<str>` в `<int>`:<br/>c = a + int(b)                                                                                                                                       |

---

2. Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие
   файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что
   в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно
   доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

````python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
````

Чтобы добиться желаемого следует убрать `break`, который прерывает цикл после первого совпадения, а также сообщать
пользователю проверяемую директорию. Флаг `is_сhange` там тоже лишний.

### Скрипт:

````python
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
````

#### Вывод скрипта:

````bash
./2.py
/home/oleg/DevOps/sysadm-homeworks/04-script-02-py/04-script-02-py/README.md
/home/oleg/DevOps/sysadm-homeworks/04-script-02-py/04-script-02-py/test.py

Process finished with exit code 0
````

---

3. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел
   воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и
   будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

Здесь будем проверять стандартные потоки, чтобы отловить ошибки, возникающие при вызове системной команды, включая "not
a git repository".

### Скрипт:

````python
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
````

#### Вывод скрипта при запуске без параметров (скрипт находится в папке, являющейся git-репозиторием, есть изменённые файлы):

````
./3.py
/home/oleg/DevOps/sysadm-homeworks/04-script-02-py/README.md
/home/oleg/DevOps/sysadm-homeworks/04-script-02-py/test.py

Process finished with exit code 0
````

#### Вывод скрипта при запуске с указанием параметра (директория не является git-репозиторием):

````
./3.py /home/oleg/bin
Error for directory /home/oleg/bin: fatal: not a git repository (or any of the parent directories): .git

Process finished with exit code 1
````

#### Вывод скрипта при запуске с указанием параметра (директория является git-репозиторием, но модифицированных файлов в ней нет):

````
./3.py /home/oleg/DevOps/devops-netology
No modified files in directory: /home/oleg/DevOps/devops-netology

Process finished with exit code 0
````

---

4. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой
   балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел,
   занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при
   этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не
   уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который
   опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>.
   Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если
   проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <
   старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com,
   google.com.

Здесь мы последовательно выполним следующие действия:

* получить IP требуемых хостов и покажем их пользователю;
* прочитаем данный предыдущих проверок из JSON-файла (если существует);
* сравним IP хостов из текущей и предыдущей проверки;
* сообщим пользователю об изменившихся IP;
* сохраним IP требуемых хостов в JSON-файл.

### Скрипт:

````python
#!/usr/bin/env python3

import json
import pathlib
import socket

# Mark for IP that not obtained.
no_ip = "UNKNOWN"

# Filename to store data to.
json_filename = 'data.json'

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
    with open('data.json', 'r') as f:
        hosts_ips_string_old = json.load(f)
        hosts_ips_old = json.loads(hosts_ips_string_old)

    # Check if IPs of the services has been changed
    hosts_ips_diff = dict()
    for key in hosts_ips_current:
        if hosts_ips_current[key] != hosts_ips_old[key]:
            hosts_ips_diff[key] = (hosts_ips_old[key], hosts_ips_current[key])

    # Inform user about changed IPs:
    for key in hosts_ips_diff:
        ips = hosts_ips_diff[key]
        print("[ERROR]{host} IP mismatch: {old} {new}".format(host=key, old=ips[0], new=ips[1]))

# Store obtained data to a file for further check.
hosts_ips_json = json.dumps(hosts_ips_current);
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(hosts_ips_json, f, ensure_ascii=False, indent=4)
````

#### Вывод скрипта:

````
./4.py
drive.google.com-64.233.162.194
mail.google.com-74.125.131.83
google.com-74.125.131.113
asdfgadsf.com-UNKNOWN
[ERROR]mail.google.com IP mismatch: 74.125.131.19 74.125.131.83
[ERROR]google.com IP mismatch: 74.125.131.100 74.125.131.113

Process finished with exit code 0
````

Как видим, в интервале проверок сервисы `mail.google.com` и `google.com` изменили свои IP-адреса.

---