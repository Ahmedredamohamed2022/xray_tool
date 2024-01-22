#!/usr/bin/env python3
import os

os.system('python readwrite_slewrate.py')
#os.system('$SAK/python/enumer.py -v -d tran/sr -r run_template.sh slewrate.spice slewrate.cfg')
os.system('./enumer.py -v -d tran/sr -r run_template.sh spice/slewrate.spice cut/ota.cfg')
directory= os.getcwd()

# path 
path1 = directory+'/tran/sr/rawfiles'
path2 = directory+'/tran/sr/rawfiles-enumer'
path3 = directory+'/tran/sr/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/tran/sr/run-all.sh ')
os.system('python readraw/slewrate_readraw.py')