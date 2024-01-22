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
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampsrpvt/rawfiles/"
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
srpos=[0]*nofile
srneg=[0]*nofile
sr=[0]*nofile
st1=[0]*nofile 
st2=[0]*nofile 
st3=[0]*nofile 
st4=[0]*nofile 
###############################################################################################
##############################################################
nofile=count
iteration=list(np.arange(nofile))
run=nofile


#str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_R2RVC/xray/vcacpvt/rawfiles/"
str1="pvt"
str2=str(1)
str3=".raw"
RESULTS_FILE=str0+str1+str2+str3
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)

read_file_no=0

for i in list(range(1,nofile+1)):
    j=i-1
    str1="pvt"
    str2=str(i)
    str3=".raw"
    RESULTS_FILE=str0+str1+str2+str3

    file_exists = os.path.exists(RESULTS_FILE)
    if file_exists==False:
        print("This file is not found:"+ str1+str2+str3)
      
    else:
      read_file_no= read_file_no+1
      print(str1+str2+str3)
      p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
      print(RESULTS_FILE)
      srposp = (p.get_datavector(0).get_data())[0]
      srnegp = (p.get_datavector(1).get_data())[0]
      srp= (p.get_datavector(2).get_data())[0]
      srpos[j]=abs(srposp)
      srneg[j]=abs(srnegp)
      sr[j]=abs(srp)  
      

###############################################################################################

#####################################################plot  srpos#########################
plt.figure(1)
plt.plot(srpos, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='srpos')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("srpos",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampsrpvt/"
plt.savefig(str0+'figures/srpos.png', dpi=300, bbox_inches='tight')
#####################################################plot  srneg#########################
plt.figure(2)
plt.plot(srneg, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='srneg')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("srneg",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampsrpvt/"
plt.savefig(str0+'figures/srneg.png', dpi=300, bbox_inches='tight')
#####################################################plot  sr#########################
plt.figure(3)
plt.plot(sr, color='black', linestyle='dashed', linewidth = 1,marker='o', markerfacecolor='blue', markersize=8,label='sr')
plt.xlabel("#corner",fontweight ="bold")
plt.ylabel("sr",fontweight ="bold")
plt.yscale("log")
plt.grid()
plt.legend()
str0="/ciic/designs/analog-mixed-signal-blocks/Xschem-schematic/EF_AMP3V3/xray/ampsrpvt/"
plt.savefig(str0+'figures/sr.png', dpi=300, bbox_inches='tight')

srtott = np.array(sr)
srtot = srtott[srtott != 0]
print(srtot)
max_srpos ="{:.2e}".format(np.max(srpos))
min_srpos = "{:.2e}".format(np.min(srpos))

max_srneg= "{:.2e}".format(np.max(srneg))
min_srneg = "{:.2e}".format(np.min(srneg))

max_sr ="{:.2e}".format(np.max(srtot))
min_sr = "{:.2e}".format(np.min(srtot))


print("max_srpos:  ",max_srpos)
print("min_srpos:  ",min_srpos)
print("max_srneg:  ",max_srneg)
print("min_srneg:  ",min_srneg)
print("max_sr:  ",max_sr)
print("min_sr:  ",min_sr)

with open('EF_AMP3V3_sr.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["corner","srpos","srneg", "sr"])
    for i in list(range(1,nofile+1)):
        j=i-1
        writer.writerow([j, "{:.2e}".format(srpos[j]),"{:.2e}".format(srneg[j]),"{:.2e}".format(sr[j])    ])
    
    writer.writerow(["max_srpos",max_srpos ])
    writer.writerow(["min_srpos",min_srpos ])
    writer.writerow(["max_sr",max_sr])
    writer.writerow(["min_sr",min_sr])
   
          
################################################## print max and min value###############################

