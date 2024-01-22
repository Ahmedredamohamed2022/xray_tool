#!/usr/bin/python
import os,sys
import spice_read
from matplotlib import pyplot as plt
import numpy as np

inoise_total_target=1e-6


thd_vi=[0]*1
thd_vo=[0]*1
########################## Read raw file ###############################################################
RESULTS_FILE = "/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/tran/thd/rawfiles/thd.raw"
x = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
########################## plot transient figure ######################################################
thd_vi[0] =  ((p.get_datavector(0).get_data())[0])
thd_vo[0] =  ((p.get_datavector(1).get_data())[0])

plt.figure(1)
#plt.plot(list(range(1,2)),avd, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='Dc_gain')
plt.title('thd_vo',fontweight ="bold",  fontsize=12)
plt.bar(list(range(1,2)),thd_vo, color='b', edgecolor='black',label='thd_vo',width = 0.1)

plt.xlabel("thd_vo",fontweight ="bold")
plt.ylabel("thd_vo (v)",fontweight ="bold")
plt.grid()
plt.axhline(y=thd_vi, color='red', linestyle="--",linewidth = 1, label='thd_vi')
plt.legend()
plt.tight_layout()
plt.autoscale() 
#plt.ylim(1e-9,1e-6)
plt.xlim(0,2)
plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/tran/thd/figures/thd_vo.png', dpi=300, bbox_inches='tight')
 ############################################
RESULTS_FILE = "/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/tran/thd/rawfiles/fft.raw"
x = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]

freq = np.array(list(p.get_scalevector().get_data()))
mag_vo= np.array(list(p.get_datavector(0).get_data()))
plt.figure(2)

plt.plot(freq,mag_vo, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='mag_vo')
plt.xlabel("Fre",fontweight ="bold")
plt.ylabel("mag_vo (v)",fontweight ="bold")
plt.grid()
plt.legend()
plt.tight_layout()
plt.autoscale() 
plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/tran/thd/figures/mag_vo.png', dpi=300, bbox_inches='tight')
 ############################################