#!/usr/bin/env python3
import os
os.system('python readwrite_psneggain.py')
directory= os.getcwd()

#os.system('$SAK/python/enumer.py -v -d ac/psneg -r run_template.sh psneggain.spice psneggain.cfg')
os.system('./enumer.py -v -d ac/psneg -r run_template.sh spice/psneggain.spice cut/ota.cfg')

# path 
path1 = directory+'/ac/psneg/rawfiles'
path2 = directory+'/ac/psneg/rawfiles-enumer'
path3 = directory+'/ac/psneg/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/ac/psneg/run-all.sh ')
os.system('python readraw/psneggain_readraw.py')