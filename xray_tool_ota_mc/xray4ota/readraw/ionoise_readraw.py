#!/usr/bin/python
import os,sys
import spice_read
from matplotlib import pyplot as plt
import numpy as np

inoise_total_target=1e-6


inoise_total=[0]*1
onoise_total=[0]*1
########################## Read raw file ###############################################################
RESULTS_FILE = "/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/noise/rawfiles/noise_total.raw"
x = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
########################## plot transient figure ######################################################
inoise_total[0] =  ((p.get_datavector(0).get_data())[0])
plt.figure(1)
#plt.plot(list(range(1,2)),avd, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='Dc_gain')
plt.title('pspos_gain',fontweight ="bold",  fontsize=12)
plt.bar(list(range(1,2)),inoise_total, color='b', edgecolor='black',label='inoise_total',width = 0.1)

plt.xlabel("inoise_total",fontweight ="bold")
plt.ylabel("inoise_total (v)",fontweight ="bold")
plt.grid()
plt.axhline(y=inoise_total_target, color='red', linestyle="--",linewidth = 1, label='inoise_total_target')
plt.legend()
plt.tight_layout()
plt.autoscale() 
#plt.ylim(1e-9,1e-6)
plt.xlim(0,2)
plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/noise/figures/inoise_total.png', dpi=300, bbox_inches='tight')
 ############################################
RESULTS_FILE = "/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/noise/rawfiles/noise_spectrum.raw"
x = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]

freq = np.array(list(p.get_scalevector().get_data()))
inoise_spectrum= np.array(list(p.get_datavector(0).get_data()))
plt.figure(2)

plt.plot(freq,inoise_spectrum, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='inoise_spectrum')
plt.xlabel("Fre",fontweight ="bold")
plt.ylabel("inoise_spectrum (v)",fontweight ="bold")
plt.grid()
plt.legend()
plt.tight_layout()
plt.autoscale() 
plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/noise/figures/inoise_spectrum.png', dpi=300, bbox_inches='tight')
 ############################################