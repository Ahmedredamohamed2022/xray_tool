#!/usr/bin/env python3
import os

os.system('$SAK/python/enumer.py -v -d ampnoisepvt -r run_template.sh ampnoisepvt.spice ampnoisepvt.cfg')
# path 
path1 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampnoisepvt/rawfiles'
path2 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampnoisepvt/rawfiles-enumer'
path3 = '/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampnoisepvt/figures'
try: 
    os.mkdir(path1) 
    os.mkdir(path2) 
    os.mkdir(path3) 
except OSError as error: 
    print(error)  
os.system('bash /ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampnoisepvt/run-all.sh ')
os.system('python readrawnoisepvt.py')