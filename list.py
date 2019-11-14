#! /usr/bin/env python
from lndynamic import LNDynamic

with open(r"/home/hme/.lunanode/commands.txt") as hpass:
    lines = hpass.readlines()

api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))
results = api.request('vm', 'list')
#print(results)
val = results.get("vms")
for i in range(0, len(val)):
    flag = 0
    for key, value in val[i].items():
        if key == 'name':
            rs = value.find("oxiane-master-")
            rt = value.find("oxiane-slave-")
            if (rs == -1 ):
                if (rt == -1):
                    break
            print('name=', value)
            user = value
        if key == 'primaryip':
            ip = value
            print('ip=', value)

#results = api.request('vm', 'info', {'vm_id': '924637f5-6b72-441b-a2c3-0a3d75dc5455'})
#print ("-----------------------")
#print (results)

#results = api.request('image', 'list')
#print(results)


#1c018f61-e116-46d2-8a64-18f6963e3be7