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
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampoffsetpvt/rawfiles/"
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

offset=[0]*nofile
vimax=[0]*nofile
vimin=[0]*nofile

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
   offsetp = (p.get_datavector(0).get_data())[0]
   viminp= (p.get_datavector(1).get_data())[0]
   vimaxp = (p.get_datavector(2).get_data())[0]


   offset[j]=np.real(offsetp)
   vimax[j]=np.real(vimaxp)
   vimin[j]=np.real(viminp)



 

#####################################################plot  ACM#########################
plt.figure(1)
plt.plot(offset, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='offset')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("offset",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampoffsetpvt/"
plt.savefig(str0+'figures/offset.png', dpi=300, bbox_inches='tight')


#####################################################plot  vimax#########################
plt.figure(2)
plt.plot(vimax, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='vimax')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("vimax",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampoffsetpvt/"
plt.savefig(str0+'figures/vimax.png', dpi=300, bbox_inches='tight')

#####################################################plot  vimin#########################
plt.figure(3)
plt.plot(vimin, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='vimin')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("vimin",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampoffsetpvt/"
plt.savefig(str0+'figures/vimin.png', dpi=300, bbox_inches='tight')


max_offset="{:.2e}".format(np.max(offset))
min_offset = "{:.2e}".format(np.min(offset))


max_vimax="{:.2e}".format(np.max(vimax))
min_vimax = "{:.2e}".format(np.min(vimax))

max_vimin="{:.2e}".format(np.max(vimin))
min_vimin = "{:.2e}".format(np.min(vimin))


print("max_offset:  ",max_offset)
print("min_offset:  ",min_offset)

print("max_vimax:  ",max_vimax)
print("min_vimax:  ",min_vimax)

print("max_vimin:  ",max_vimin)
print("min_vimin:  ",min_vimin)
 
with open('EF_AMP3V3_offset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["corner","offset","vimax","vimin"])
    for i in list(range(1,nofile+1)):
        j=i-1
        writer.writerow([j, "{:.2e}".format(offset[j]),"{:.2e}".format(vimax[j]),"{:.2e}".format(vimin[j]) ])
    
    writer.writerow(["max_offset",max_offset ])
    writer.writerow(["min_offset",min_offset ])
     
    writer.writerow(["max_vimax",max_vimax ])
    writer.writerow(["min_vimax",min_vimax ])
     
    writer.writerow(["max_vimin",max_vimin ])
    writer.writerow(["min_vimin",min_vimin ])
     