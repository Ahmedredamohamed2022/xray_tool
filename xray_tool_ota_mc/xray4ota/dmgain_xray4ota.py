#!/usr/bin/env python3
import os

os.system('python readwrite_dmgain.py')

#os.system('$SAK/python/enumer.py -v -d ac/dm -r run_template.sh dmgain.spice dmgain.cfg')
os.system('./enumer.py -v -d ac/dm -r run_template.sh spice/dmgain.spice cut/ota.cfg')
directory= os.getcwd()
print(directory)
# path 
path1 = directory+'/ac/dm/rawfiles'
path2 = directory+'/ac/dm/rawfiles-enumer'
path3 = directory+'/ac/dm/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/ac/dm/run-all.sh ')
os.system('python readraw/dmgain_readraw.py')