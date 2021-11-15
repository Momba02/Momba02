import paramiko
from paramiko import *
host = "192.168.56.102"
port = 22
username = "root"
password = "Ronron162534"
command = "ls -la"
ssh =paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(host,port,username,password)

stdin,stdout,stderr = ssh.exec_command(command)
line =stdout.readlines()
print(line)
