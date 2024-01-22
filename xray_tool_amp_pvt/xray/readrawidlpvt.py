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
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampidlpvt/rawfiles/"
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

idl=[0]*nofile

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
   idlp = (p.get_datavector(0).get_data())[0]
   

   idl[j]=np.real(idlp)
    


 

#####################################################plot  ACM#########################
plt.figure(1)
plt.plot(idl, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='IDL')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("idl",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampidlpvt/"
plt.savefig(str0+'figures/idl.png', dpi=300, bbox_inches='tight')



max_idl="{:.2e}".format(np.max(idl))
min_idl = "{:.2e}".format(np.min(idl))


print("max_idl:  ",max_idl)
print("min_idl:  ",min_idl)
 
with open('EF_AMP3V3_cm.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["corner","idl"])
    for i in list(range(1,nofile+1)):
        j=i-1
        writer.writerow([j, "{:.2e}".format(idl[j])])
    
    writer.writerow(["max_idl",max_idl ])
    writer.writerow(["min_idl",min_idl ])
     
################################################## print max and min value###############################

