#!/usr/bin/env python3
import os
os.system('python readwrite_psposgain.py')

#os.system('$SAK/python/enumer.py -v -d ac/pspos -r run_template.sh psposgain.spice psposgain.cfg')
os.system('./enumer.py -v -d ac/pspos -r run_template.sh spice/psposgain.spice cut/ota.cfg')
directory= os.getcwd()

# path 
path1 = directory+'/ac/pspos/rawfiles'
path2 = directory+'/ac/pspos/rawfiles-enumer'
path3 = directory+'/ac/pspos/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/ac/pspos/run-all.sh ')
os.system('python readraw/psposgain_readraw.py')