#!/usr/bin/python
import os,sys
import spice_read
from matplotlib import pyplot as plt
import numpy as np

i_budget=5e-3
no_mosfer_per_ota=8
id= [0]*no_mosfer_per_ota
gm= [0]*no_mosfer_per_ota
gm_id= [0]*no_mosfer_per_ota
itot=[0]*1
ptot=[0]*1
########################## Read raw file ###############################################################
RESULTS_FILE = "/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/dc/op/rawfiles/dcop.raw"
x = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
########################## plot transient figure ######################################################
#time = np.array(list(p.get_scalevector().get_data()))
#vin = np.array(list(p.get_datavector(6).get_data()))
#vout = np.array(list(p.get_datavector(7).get_data()))
#######################################################################################################
########################## calculate the measured paramters tf,tr,tp,pw, and PDP ######################
for i in list(range(1,no_mosfer_per_ota+1)):
   j=i-1
   #gm[j] = "{:.2e}".format((p.get_datavector((i-1)*2).get_data())[0])
   #id[j] = "{:.2e}".format((p.get_datavector(((i-1)*2)+1).get_data())[0])
   #gm_id[j]=float(gm[j])/float(id[j])
   
itot[0]= "{:.2e}".format((p.get_datavector(0).get_data())[0])
ptot= "{:.2e}".format((p.get_datavector(1).get_data())[0])


plt.figure(4)
plt.plot(list(range(1,2)),itot, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='i_total')
plt.title('MOSFET_Current',fontweight ="bold",  fontsize=12)
plt.xlabel("ota",fontweight ="bold")
plt.ylabel("i_total (A)",fontweight ="bold")
plt.grid()
plt.axhline(y=i_budget, color='red', linestyle="--",linewidth = 1, label='i_budget')
plt.legend()

plt.savefig('/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/ota-2stage/xray4ota/dc/op/figures/i_total.png', dpi=300, bbox_inches='tight')
