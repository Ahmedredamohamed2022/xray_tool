#!/usr/bin/python
import os,sys
import spice_read
from matplotlib import pyplot as plt
import numpy as np

avd_target=50
gbw_target=2*1e7
pm_target=50
bw_target=3*1e3

avd=[0]*1
gbw=[0]*1
pm=[0]*1
bw=[0]*1
########################## Read raw file ###############################################################
RESULTS_FILE = "/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/dm/rawfiles/dmgain.raw"
x = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
########################## plot transient figure ######################################################
freq = (list(abs(p.get_scalevector().get_data())))
avd_db = (list(abs(p.get_datavector(0).get_data())))
pm_deg = np.array(list(p.get_datavector(1).get_data()))
#######################################################################################################
########################## avdm gbwpm bw ######################
#avd[0] =  ("{:.2e}".format(abs((p.get_datavector(2).get_data())[0])))
avd[0] =  abs((p.get_datavector(2).get_data())[0])
#gbw[0]=  ("{:.2e}".format(abs((p.get_datavector(3).get_data())[0])))
gbw[0]=  abs((p.get_datavector(3).get_data())[0])
#pm[0]=  ("{:.2e}".format(abs((p.get_datavector(4).get_data())[0])))
pm[0]=  abs((p.get_datavector(4).get_data())[0])
bw[0] =  abs((p.get_datavector(5).get_data())[0])

#bw[0] =  ("{:.2e}".format(abs((p.get_datavector(5).get_data())[0])))

############################################avd and pm vs freq ####################################
plt.figure(1)
#plt.bar(list(range(1,2)),avd, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='Dc_gain')
plt.title('dc_gain',fontweight ="bold",  fontsize=12)
plt.bar(list(range(1,2)),avd, color='b', edgecolor='black',label='Dc_gain',width = 0.1)

plt.xlabel("dc_gain",fontweight ="bold")
plt.ylabel("dc_gain (dB)",fontweight ="bold")
plt.grid()
plt.axhline(y=avd_target, color='red', linestyle="--",linewidth = 1, label='avd_target')
plt.legend()
plt.tight_layout()
plt.autoscale() 
#plt.ylim(1e-9,1e-6)
plt.xlim(0,2)
plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/dm/figures/dcgain.png', dpi=300, bbox_inches='tight')
 ############################################
plt.figure(2)
#plt.plot(list(range(1,2)),gbw, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='gain_bandwidth_product')
plt.bar(list(range(1,2)),gbw, color='r', edgecolor='black',label='gbw',width = 0.1)

plt.title('gbw',fontweight ="bold",  fontsize=12)
plt.xlabel("gbw",fontweight ="bold")
plt.ylabel("gbw (Hz)",fontweight ="bold")
plt.grid()
plt.axhline(y=gbw_target, color='red', linestyle="--",linewidth = 1, label='gbw_target')
plt.legend()
plt.autoscale() 
plt.xlim(0,2)

plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/dm/figures/gbw.png', dpi=300, bbox_inches='tight')
 ############################################
plt.figure(3)
#plt.plot(list(range(1,2)),pm, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='phase_margin')
plt.bar(list(range(1,2)),pm, color='b', edgecolor='black',label='pm',width = 0.1)

plt.title('phase_margin',fontweight ="bold",  fontsize=12)
plt.xlabel("phase_margin",fontweight ="bold")
plt.ylabel("phase_margin (deg)",fontweight ="bold")
plt.grid()
plt.axhline(y=pm_target, color='red', linestyle="--",linewidth = 1, label='pm_target')
plt.legend()
plt.autoscale() 
plt.xlim(0,2)

plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/dm/figures/pm.png', dpi=300, bbox_inches='tight')
 ############################################

plt.figure(4)
#plt.plot(list(range(1,2)),pm, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='bandwidth')
plt.bar(list(range(1,2)),bw, color='g', edgecolor='black',label='bw',width = 0.1)

plt.title('band_width',fontweight ="bold",  fontsize=12)
plt.xlabel("band_width",fontweight ="bold")
plt.ylabel("band_width (Hz)",fontweight ="bold")
plt.grid()
plt.axhline(y=bw_target, color='red', linestyle="--",linewidth = 1, label='bw_target')
plt.legend()
plt.autoscale() 
plt.xlim(0,2)

plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/ac/dm/figures/bw.png', dpi=300, bbox_inches='tight')
 
