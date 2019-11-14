# install-postgresql-lunanode

## playbook
Postgresql12 installation is performed by using the command ansible-playbook with the following inventory
file format :
```ini
[local]
localhost  ansible_connection=local  ansible_python_interpreter="/usr/bin/env python"
[lunanode]
xx.xxx.xxx.xx  ansible_ssh_user=test  ansible_ssh_pass=test ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
xx.xxx.xx.xx   ansible_ssh_user=test  ansible_ssh_pass=test ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
xx.xxx.xx.xx   ansible_ssh_user=test  ansible_ssh_pass=test ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
``` 
 
