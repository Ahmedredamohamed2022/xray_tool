#!/usr/bin/python
import os,sys
import spice_read
import string
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import stats
import matplotlib.mlab as mlab
import csv
################################################################ count no rawfiles######################
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampdmpvt/rawfiles/"
dir_path = str0
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
##############################################################
nofile=count

print(nofile)

dcgain=[0]*nofile
bw=[0]*nofile
gbw=[0]*nofile
pm=[0]*nofile 

#str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_R2RVC/xray/vcacpvt/rawfiles/"
str1="pvt"
str2=str(1)
str3=".raw"
RESULTS_FILE=str0+str1+str2+str3
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)

for i in list(range(1,nofile+1)):
   j=i-1
   str1="pvt"
   str2=str(i)
   str3=".raw"
   RESULTS_FILE=str0+str1+str2+str3
   print(RESULTS_FILE)
   p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
   dcgainp = (p.get_datavector(0).get_data())[0]
   bwp = (p.get_datavector(1).get_data())[0]
   gbwp= (p.get_datavector(2).get_data())[0]
   pmp= (p.get_datavector(3).get_data())[0]
   #ih=  (p.get_datavector(4).get_data())[0]
   #il=  (p.get_datavector(5).get_data())[0]

   dcgain[j]=abs(dcgainp)
   bw[j]=abs(bwp)
   gbw[j]=abs(gbwp)
   pm[j]=abs(pmp)



print(dcgain)
print(bw)
print(gbw)
print(pm)


#####################################################plot  dcgain#########################
plt.figure(1)
plt.plot(dcgain, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='dcgain')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("dcgain",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampdmpvt/"
plt.savefig(str0+'figures/dcgain.png', dpi=300, bbox_inches='tight')
#####################################################plot  bw#########################
plt.figure(2)
plt.plot(bw, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='bw')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("bw",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampdmpvt/"
plt.savefig(str0+'figures/bw.png', dpi=300, bbox_inches='tight')
#####################################################plot  gbw#########################
plt.figure(3)
plt.plot(gbw, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='gbw')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("gbw",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampdmpvt/"
plt.savefig(str0+'figures/gbw.png', dpi=300, bbox_inches='tight')
#####################################################plot  tph2l#########################
plt.figure(4)
plt.plot(pm, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='pm')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("pm",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampdmpvt/"
plt.savefig(str0+'figures/pm.png', dpi=300, bbox_inches='tight')


max_dcgain ="{:.2e}".format(np.max(dcgain))
min_dcgain = "{:.2e}".format(np.min(dcgain))

max_bw= "{:.2e}".format(np.max(bw))
min_bw = "{:.2e}".format(np.min(bw))

max_gbw ="{:.2e}".format(np.max(gbw))
min_gbw = "{:.2e}".format(np.min(gbw))

max_pm= "{:.2e}".format(np.max(pm))
min_pm = "{:.2e}".format(np.min(pm))

print("max_dcgain:  ",max_dcgain)
print("min_dcgain:  ",min_dcgain)
print("max_bw:  ",max_bw)
print("min_bw:  ",min_bw)
print("max_gbw:  ",max_gbw)
print("min_gbw:  ",min_gbw)
print("max_pm:  ",max_pm)
print("min_pm:  ",min_pm)
with open('EF_AMP3V3_dm.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["corner","dcgain","bw", "gbw","pm"])
    for i in list(range(1,nofile+1)):
        j=i-1
        writer.writerow([j, "{:.2e}".format(dcgain[j]),"{:.2e}".format(bw[j]),"{:.2e}".format(gbw[j]),"{:.2e}".format(pm[j])    ])
    
    writer.writerow(["max_dcgain",max_dcgain ])
    writer.writerow(["min_dcgain",min_dcgain ])
    writer.writerow(["max_bw",max_bw])
    writer.writerow(["min_bw",min_bw])
    writer.writerow(["max_gbw",max_gbw])
    writer.writerow(["min_gbw",min_gbw])  
    writer.writerow(["max_pm",max_pm ])
    writer.writerow(["min_pm",min_pm ])  
################################################## print max and min value###############################

