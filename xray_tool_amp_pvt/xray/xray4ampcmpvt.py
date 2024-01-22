#!/usr/bin/env python3
import os

os.system('$SAK/python/enumer.py -v -d ampcmpvt -r run_template.sh ampcmpvt.spice ampcmpvt.cfg')
# path 
path1 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampcmpvt/rawfiles'
path2 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampcmpvt/rawfiles-enumer'
path3 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampcmpvt/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash /ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampcmpvt/run-all.sh ')
os.system('python readrawcmpvt.py')