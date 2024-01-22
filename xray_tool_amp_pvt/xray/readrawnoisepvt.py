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
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampnoisepvt/rawfiles/"
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

noise=[0]*nofile

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
   noisep = (p.get_datavector(0).get_data())[0]
   

   noise[j]=np.real(noisep)
    


 

#####################################################plot  #########################
plt.figure(1)
plt.plot(noise, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='inoise_total')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("inoise_total",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampnoisepvt/"
plt.savefig(str0+'figures/inoise_total.png', dpi=300, bbox_inches='tight')



max_noise ="{:.2e}".format(np.max(noise))
min_noise = "{:.2e}".format(np.min(noise))


print("max_noise:  ",max_noise)
print("min_noise:  ",min_noise)
 
with open('EF_AMP3V3_noise.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["corner","noise"])
    for i in list(range(1,nofile+1)):
        j=i-1
        writer.writerow([j, "{:.2e}".format(noise[j])])
    
    writer.writerow(["max_noise",max_noise ])
    writer.writerow(["min_noise",min_noise ])
     
################################################## print max and min value###############################

