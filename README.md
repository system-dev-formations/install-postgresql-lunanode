# install-k8s-lunanode

This repository is here to set up a sandbox to train kubernetes students. Couple of  
scripts create the environment in Lunanode, a canadian ISP, with lowcd .. price for virtual machines  
see their website [here](https://www.lunanode.com/).

## First create all cluster VMs 
Get an API credentials from the lunanode website, see [here](https://dynamic.lunanode.com/panel/api)  
Save your API credentials in a file under your $HOME directory, change the line 7 in the file 
`create_vm_cluster.py` accordingly to your environment.  
Hit `create_vm_cluster.py`.  A prompt asks you for how many students you want to set up a cluster. 
4 Vms, one master, and 3 nodes will be created soon after for each student.   
Each VM has 3 cores, and 4 Gb of RAM.  
 
