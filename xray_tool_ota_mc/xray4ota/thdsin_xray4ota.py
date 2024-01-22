#!/usr/bin/env python3
import os
os.system('python readwrite_thdsin.py')
#os.system('$SAK/python/enumer.py -v -d tran/thd -r run_template.sh thdsin.spice thdsin.cfg')
os.system('./enumer.py -v -d tran/thd -r run_template.sh spice/thdsin.spice cut/ota.cfg')
directory= os.getcwd()

# path 
path1 = directory+'/tran/thd/rawfiles'
path2 = directory+'/tran/thd/rawfiles-enumer'
path3 = directory+'/tran/thd/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/tran/thd/run-all.sh ')
os.system('python readraw/thdsin_readraw.py')