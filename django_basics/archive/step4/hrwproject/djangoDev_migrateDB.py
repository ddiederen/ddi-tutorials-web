# import subprocess
import os

# input
apps =  ['','hrwapp1',]  # '' is the project app
databases = ['default','hrwapp1_db',]

# make migrations
for app in apps:
    cmd = 'python manage.py makemigrations '+app
    os.system(cmd)
    # print(subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout.read())

# migrate to databases
for database in databases:
    cmd = 'python manage.py migrate --database='+database
    os.system(cmd)
    # print(subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout.read())
