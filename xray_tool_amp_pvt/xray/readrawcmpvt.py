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
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampcmpvt/rawfiles/"
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

acm=[0]*nofile

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
   acmp = (p.get_datavector(0).get_data())[0]
   

   acm[j]=np.real(acmp)
    


 

#####################################################plot  ACM#########################
plt.figure(1)
plt.plot(acm, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='ACM')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("acm",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampcmpvt/"
plt.savefig(str0+'figures/dcgain.png', dpi=300, bbox_inches='tight')



max_acm ="{:.2e}".format(np.max(acm))
min_acm = "{:.2e}".format(np.min(acm))


print("max_acm:  ",max_acm)
print("min_acm:  ",min_acm)
 
with open('EF_AMP3V3_cm.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["corner","acm"])
    for i in list(range(1,nofile+1)):
        j=i-1
        writer.writerow([j, "{:.2e}".format(acm[j])])
    
    writer.writerow(["max_acm",max_acm ])
    writer.writerow(["min_acm",min_acm ])
     
################################################## print max and min value###############################

