#!/usr/bin/env python3
import os

os.system('python readwrite_offset.py')
#os.system('$SAK/python/enumer.py -v -d dc/offset -r run_template.sh offset.spice offset.cfg')
os.system('./enumer.py -v -d dc/offset -r run_template.sh spice/offset.spice cut/ota.cfg')
directory= os.getcwd()
# path 
path1 = directory+'/dc/offset/rawfiles'
path2 = directory+'/dc/offset/rawfiles-enumer'
path3 = directory+'/dc/offset/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/dc/offset/run-all.sh ')
os.system('python readraw/offset_readraw.py')