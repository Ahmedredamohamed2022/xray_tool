#!/usr/bin/python
import os,sys
import spice_read
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import stats
import matplotlib.mlab as mlab


with open("cut/specifications.txt", "r") as file:
    spec=file.read().splitlines()
    print(spec)
USLAV=float(spec[3])
LSLAV=float(spec[5])
USLGBW=float(spec[7])
LSLGBW=float(spec[9])
USLPM=float(spec[11])
LSLPM=float(spec[13])

#USLAV=100
#LSLAV=0
#USLGBW=50e6
#LSLGBW=1e6

#USLPM=90
#LSLPM=45

################################################################ count no rawfiles######################
str0="ac/dmmc/rawfiles/"
dir_path = str0
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
##############################################################
#nofile=int(nosupplyvariaiton*nocorners*notemp)
nofile=count
iteration=list(np.arange(nofile))
run=nofile
#binhg=30  for run=100
binhg=30  #for run=10

avmc= [0]*run
gbwmc= [0]*run
pmmc= [0]*run
str0="ac/dmmc/rawfiles/"
str1="dmmc"
str2=str(1)
str3=".raw"
RESULTS_FILE=str0+str1+str2+str3
os.system('chmod +x spice_read.py ')
os.system('./spice_read.py '+RESULTS_FILE)
read_file_no=0
for i in list(range(1,nofile+1)):
    j=i-1
    str1="dmmc"
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
      p = spice_read.spice_read(RESULTS_FILE).get_plots()[0]
      av = (p.get_datavector(0).get_data())[0]
      gbw = (p.get_datavector(1).get_data())[0]
      pm= (p.get_datavector(2).get_data())[0]
      avmc[j]=abs(av)
      gbwmc[j]=abs(gbw)
      pmmc[j]=abs(pm)
      print (avmc)
      print (gbwmc)
      print (pmmc)

####################################################### AV ###################################################
plt.figure(1)
n,b,patches=plt.hist(avmc, bins = binhg, histtype ='bar',align='mid',edgecolor='black', linewidth=2, rwidth=0.5, color ='blue', label='Histogram')
std="{:.2e}".format(np.std(avmc))
mean="{:.2e}".format(np.mean(avmc))
print("Standard Deviation of the sample is :" + str(std))
print("Mean of the sample is:" + str(mean) ) 
plt.grid()
plt.legend()  
#plt.title("run= %d "% run + ", \u03BC = " +str(mean)+ ", \u03C3= " +str(std),fontweight ="bold")
plt.xlabel("open loop gain",fontweight ="bold")
plt.ylabel("#Sample",fontweight ="bold")
##################################################### add a 'best fit' line
#xmin=float(mean)-6*float(std)
#xmax=float(mean)+6*float(std)
#x=np.linspace(xmin, xmax,50)
#y = mlab.normpdf(x, float(mean),float(std))
#plt.plot(x, (y/max(y))*max(n), 'r--', label='Fitted function')
#plt.xlim((0, xmax))
#plt.grid()
#plt.legend()

###################################################### proecss  capablity  
plt.axvline(x=USLAV, color='blue', linestyle="--",linewidth = 1)
plt.axvline(x=LSLAV, color='blue',linestyle="--",linewidth = 1)
plt.text(USLAV, max(n)/2, 'USL', ha='center', va='center',fontweight ="bold")
plt.text(LSLAV, max(n)/2, 'LSL', ha='center', va='center',fontweight ="bold")
cp= (USLAV-LSLAV)/(6*float(std))
cp="{:.2f}".format(cp)
cpu=(USLAV-float(mean))/(3*float(std))
cpl=(float(mean)-LSLAV)/(3*float(std))
cpk=min(cpu,cpl)
cpk="{:.2f}".format(cpk)
plt.title("run= %d "% run + ", \u03BC = " +str(mean)+ ", \u03C3= " +str(std)+"\n Cp= "+str(cp)+" ,cpk= "+str(cpk),fontweight ="bold")
plt.savefig('ac/dmmc/figures/av.png', dpi=300, bbox_inches='tight')

Summary = open('ac/dmmc/00000/mcav.txt','w')
Summary.write(str(read_file_no))
Summary.write("\n")
Summary.write(mean)
Summary.write("\n")
Summary.write(std)
Summary.write("\n")
Summary.write(cp)
Summary.write("\n")
Summary.write(cpk)
#########################################################################
Summary.close()


####################################################### GBW ###################################################
plt.figure(2)
n,b,patches=plt.hist(gbwmc, bins = binhg, histtype ='bar',align='mid',edgecolor='black', linewidth=2, rwidth=0.5, color ='blue', label='Histogram')
std="{:.2e}".format(np.std(gbwmc))
mean="{:.2e}".format(np.mean(gbwmc))
print("Standard Deviation of the sample is :" + str(std))
print("Mean of the sample is:" + str(mean) ) 
plt.grid()
plt.legend()  
#plt.title("run= %d "% run + ", \u03BC = " +str(mean)+ ", \u03C3= " +str(std),fontweight ="bold")
plt.xlabel("Gain bandwidth product",fontweight ="bold")
plt.ylabel("#Sample",fontweight ="bold")
##################################################### add a 'best fit' line
#xmin=float(mean)-6*float(std)
#xmax=float(mean)+6*float(std)
#x=np.linspace(xmin, xmax,50)
#y = mlab.normpdf(x, float(mean),float(std))
#plt.plot(x, (y/max(y))*max(n), 'r--', label='Fitted function')
#plt.xlim((0, xmax))
#plt.grid()
#plt.legend()

###################################################### proecss  capablity  
plt.axvline(x=USLGBW, color='blue', linestyle="--",linewidth = 1)
plt.axvline(x=LSLGBW, color='blue',linestyle="--",linewidth = 1)
plt.text(USLGBW, max(n)/2, 'USL', ha='center', va='center',fontweight ="bold")
plt.text(LSLGBW, max(n)/2, 'LSL', ha='center', va='center',fontweight ="bold")
cp= (USLGBW-LSLGBW)/(6*float(std))
cp="{:.2f}".format(cp)
cpu=(USLGBW-float(mean))/(3*float(std))
cpl=(float(mean)-LSLGBW)/(3*float(std))
cpk=min(cpu,cpl)
cpk="{:.2f}".format(cpk)
plt.title("run= %d "% run + ", \u03BC = " +str(mean)+ ", \u03C3= " +str(std)+"\n Cp= "+str(cp)+" ,cpk= "+str(cpk),fontweight ="bold")
plt.savefig('ac/dmmc/figures/gbw.png', dpi=300, bbox_inches='tight')

Summary = open('ac/dmmc/00000/mcgbw.txt','w')
Summary.write(str(read_file_no))
Summary.write("\n")
Summary.write(mean)
Summary.write("\n")
Summary.write(std)
Summary.write("\n")
Summary.write(cp)
Summary.write("\n")
Summary.write(cpk)
#########################################################################
Summary.close()



####################################################### PM ###################################################
plt.figure(3)
n,b,patches=plt.hist(pmmc, bins = binhg, histtype ='bar',align='mid',edgecolor='black', linewidth=2, rwidth=0.5, color ='blue', label='Histogram')
std="{:.2e}".format(np.std(pmmc))
mean="{:.2e}".format(np.mean(pmmc))
print("Standard Deviation of the sample is :" + str(std))
print("Mean of the sample is:" + str(mean) ) 
plt.grid()
plt.legend()  
#plt.title("run= %d "% run + ", \u03BC = " +str(mean)+ ", \u03C3= " +str(std),fontweight ="bold")
plt.xlabel("Phase Margin",fontweight ="bold")
plt.ylabel("#Sample",fontweight ="bold")
##################################################### add a 'best fit' line
#xmin=float(mean)-6*float(std)
#xmax=float(mean)+6*float(std)
#x=np.linspace(xmin, xmax,50)
#y = mlab.normpdf(x, float(mean),float(std))
#plt.plot(x, (y/max(y))*max(n), 'r--', label='Fitted function')
#plt.xlim((0, xmax))
#plt.grid()
#plt.legend()

###################################################### proecss  capablity  
plt.axvline(x=USLPM, color='blue', linestyle="--",linewidth = 1)
plt.axvline(x=LSLPM, color='blue',linestyle="--",linewidth = 1)
plt.text(USLPM, max(n)/2, 'USL', ha='center', va='center',fontweight ="bold")
plt.text(LSLPM, max(n)/2, 'LSL', ha='center', va='center',fontweight ="bold")
cp= (USLPM-LSLPM)/(6*float(std))
cp="{:.2f}".format(cp)
cpu=(USLPM-float(mean))/(3*float(std))
cpl=(float(mean)-LSLPM)/(3*float(std))
cpk=min(cpu,cpl)
cpk="{:.2f}".format(cpk)
plt.title("run= %d "% run + ", \u03BC = " +str(mean)+ ", \u03C3= " +str(std)+"\n Cp= "+str(cp)+" ,cpk= "+str(cpk),fontweight ="bold")
plt.savefig('ac/dmmc/figures/pm.png', dpi=300, bbox_inches='tight')

Summary = open('ac/dmmc/00000/mcpm.txt','w')
Summary.write(str(read_file_no))
Summary.write("\n")
Summary.write(mean)
Summary.write("\n")
Summary.write(std)
Summary.write("\n")
Summary.write(cp)
Summary.write("\n")
Summary.write(cpk)
#########################################################################
Summary.close()
