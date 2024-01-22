#!/usr/bin/env python3
import os
os.system('python readwrite_ionoise.py')

#os.system('$SAK/python/enumer.py -v -d ac/noise -r run_template.sh ionoise.spice ionoise.cfg')
os.system('./enumer.py -v -d ac/noise -r run_template.sh spice/ionoise.spice cut/ota.cfg')
directory= os.getcwd()
print(directory)
# path 
path1 = directory+'/ac/noise/rawfiles'
path2 = directory+'/ac/noise/rawfiles-enumer'
path3 = directory+'/ac/noise/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash '+directory+'/ac/noise/run-all.sh ')
os.system('python readraw/ionoise_readraw.py')