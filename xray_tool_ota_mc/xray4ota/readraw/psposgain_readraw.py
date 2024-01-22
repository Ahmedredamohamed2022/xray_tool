#!/usr/bin/python
import os,sys
import spice_read
from matplotlib import pyplot as plt
import numpy as np

pspos_target=-10


pspos=[0]*1
########################## Read raw file ###############################################################
RESULTS_FILE = "/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/pspos/rawfiles/psposgain.raw"
x = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
########################## plot transient figure ######################################################
pspos[0] =  ((p.get_datavector(0).get_data())[0])

plt.figure(1)
#plt.bar(list(range(1,2)),avd, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='Dc_gain')
plt.title('pspos_gain',fontweight ="bold",  fontsize=12)
plt.bar(list(range(1,2)),pspos, color='b', edgecolor='black',label='cm_gain',width = 0.1)

plt.xlabel("pspos_gain",fontweight ="bold")
plt.ylabel("pspos_gain (dB)",fontweight ="bold")
plt.grid()
plt.axhline(y=pspos_target, color='red', linestyle="--",linewidth = 1, label='pspos_target')
plt.legend()
plt.tight_layout()
plt.autoscale() 
#plt.ylim(1e-9,1e-6)
plt.xlim(0,2)
plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/pspos/figures/psposgain.png', dpi=300, bbox_inches='tight')
 ############################################