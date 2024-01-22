#!/usr/bin/env python3
import os

os.system('python readwrite_qpoint.py')
#os.system('$SAK/python/enumer.py -v -d dc/op -r run_template.sh qpoint.spice qpoint.cfg')
os.system('./enumer.py -v -d dc/op -r run_template.sh spice/qpoint.spice cut/ota.cfg')

directory= os.getcwd()
print(directory)
# path 
path1 = directory+'/dc/op/rawfiles'
path2 = directory+'/dc/op/rawfiles-enumer'
path3 = directory+'/dc/op/figures'

try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/dc/op/run-all.sh ')
os.system('python readraw/qpoint_readraw.py')