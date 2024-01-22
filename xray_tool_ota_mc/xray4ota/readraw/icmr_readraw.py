#!/usr/bin/python
import os,sys
import spice_read
from matplotlib import pyplot as plt
import numpy as np

vimin_target=0.3


vimin=[0]*1
 ########################## Read raw file ###############################################################
RESULTS_FILE = "/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/dc/icmr/rawfiles/icmr.raw"
x = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
########################## plot transient figure ######################################################
vimin[0] =  ((p.get_datavector(0).get_data())[0])
 
plt.figure(1)
#plt.plot(list(range(1,2)),avd, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='Dc_gain')
plt.title('offset',fontweight ="bold",  fontsize=12)
plt.bar(list(range(1,2)),vimin, color='b', edgecolor='black',label='vimin',width = 0.1)

plt.xlabel("vimin",fontweight ="bold")
plt.ylabel("vimin (v)",fontweight ="bold")
plt.grid()
plt.axhline(y= vimin_target, color='red', linestyle="--",linewidth = 1, label='vimin_target')
plt.legend()
plt.tight_layout()
plt.autoscale() 
#plt.ylim(1e-9,1e-6)
plt.xlim(0,2)
plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/dc/icmr/figures/vimin.png', dpi=300, bbox_inches='tight')
 ############################################
