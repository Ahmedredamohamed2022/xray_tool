#!/usr/bin/env python3
import os

os.system('$SAK/python/enumer.py -v -d amppsrpvt -r run_template.sh amppsrpvt.spice amppsrpvt.cfg')
# path 
path1 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/amppsrpvt/rawfiles'
path2 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/amppsrpvt/rawfiles-enumer'
path3 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/amppsrpvt/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash /ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/amppsrpvt/run-all.sh ')
os.system('python readrawpsrpvt.py')