#!/usr/bin/env python
from lndynamic import LNDynamic
import natsort
import time

# find lunanode credentials
with open(r"/home/hme/.lunanode/commands.txt") as hpass:
    lines = hpass.readlines()
api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))

cluster_name = 'k8s-green-'
results = api.request('vm', 'list')
f = open(r"/home/hme/inventory_lunanode_green", "w+")
hfile = open(r"/home/hme/user_list_k8s_green", "w+")
val = results.get("vms")
user_dic = {}
print
len(val)
for i in range(0, len(val)):
    flag = 0
    for key, value in val[i].items():
        if key == 'name':
            if cluster_name not in value:
                break
            print('name=', value)
            user = value
        if key == 'primaryip':
            ip = value
            print('ip=', value)
        if key == 'plan_id':
            print('plan_id=', value)
        if key == 'vm_id':
            print('vm_id=', value)
            vm_info = api.request('vm', 'info', {'vm_id': value})
            st = vm_info.get('info')
            try:
                print(st['login_details'])
                user_login = st['login_details']
                a = user_login.split()
                print(str(ip), str(a[1]), str(a[3]))
                gt = str(a[1])[:-1]
                line = "{}  ansible_ssh_user={}  ansible_ssh_pass={} ansible_ssh_extra_args='-o StrictHostKeyChecking=no'\n".format(
                    str(ip), str(gt), str(a[3]))
                f.write(line)
                user_dic[str(user)] = str(ip)
            except KeyError as error:
                pass

f.close()
# print (user_dic)
list_user = user_dic.keys();
natural = natsort.natsorted(list_user)
# print natural
for vts in range(0, len(natural)):
    myip = user_dic[natural[vts]]
    user_line = "{} \t {} \t centos \n".format(natural[vts], myip)
    hfile.write(user_line)
hfile.close()
