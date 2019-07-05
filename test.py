# import paramiko

# ip_address = "10.63.209.126"
# port       = "2222"
# username   = "admin"
# password   = "admin"

# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(ip_address, port=port, username=username, password=password)

# stdin, stdout, stderr = client.exec_command("ls -l")
# for line in stdout.read().splitlines():
#     print (line)


from folder import Folder
from sync   import Sync

import os
os.system("python reset.py")


source = Folder("./test_folder/source/")
target = Folder("./test_folder/target/")

sync = Sync(source, target)
sync.synchronize()
