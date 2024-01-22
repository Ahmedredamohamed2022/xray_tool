#!/usr/bin/env python3
import os

os.system('python readwrite_cmgain.py')
#os.system('$SAK/python/enumer.py -v -d ac/cm -r run_template.sh cmgain.spice cmgain.cfg')
os.system('./enumer.py -v -d ac/cm -r run_template.sh spice/cmgain.spice cut/ota.cfg')
directory= os.getcwd()
print(directory)
# path 
path1 = directory+'/ac/cm/rawfiles'
path2 = directory+'/ac/cm/rawfiles-enumer'
path3 = directory+'/ac/cm/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/ac/cm/run-all.sh ')
os.system('python readraw/cmgain_readraw.py')