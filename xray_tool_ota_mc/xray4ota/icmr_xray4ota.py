#!/usr/bin/env python3
import os
os.system('python readwrite_icmr.py')

#os.system('$SAK/python/enumer.py -v -d dc/icmr -r run_template.sh icmr.spice icmr.cfg')
os.system('./enumer.py -v -d dc/icmr -r run_template.sh spice/icmr.spice cut/ota.cfg')
directory= os.getcwd()
print(directory)
# path 
path1 = directory+'/dc/icmr/rawfiles'
path2 = directory+'/dc/icmr/rawfiles-enumer'
path3 = directory+'/dc/icmr/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/dc/icmr/run-all.sh ')
os.system('python readraw/icmr_readraw.py')