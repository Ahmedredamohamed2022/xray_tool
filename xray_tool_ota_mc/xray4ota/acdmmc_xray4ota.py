#!/usr/bin/env python3
import os
os.system('python readwrite_acdmmc.py')
#os.system('$SAK/python/enumer.py -v -d ac/dm -r run_template.sh dmgain.spice dmgain.cfg')
os.system('./enumer.py -v -d ac/dmmc -r run_template.sh spice/acdmmc.spice cut/ota.cfg')
directory= os.getcwd()
print(directory)
# path 
path1 = directory+'/ac/dmmc/rawfiles'
path2 = directory+'/ac/dmmc/rawfiles-enumer'
path3 = directory+'/ac/dmmc/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/ac/dmmc/run-all.sh ')
os.system('python readraw/acdmmc_readraw.py')