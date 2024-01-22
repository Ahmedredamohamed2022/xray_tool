#!/usr/bin/env python3
import os
from pathlib import Path

directory= os.getcwd()
print(directory)
path1 = directory+'/summary'

try: 
    os.mkdir(path1)

except OSError as error: 
    print(error)  

################################# Read structure of OTA ################

with open("cut/specifications.txt", "r") as file:
    spec=file.read().splitlines()
name_stru=spec[1]
cl=float(spec[15])
################################# xraty for DC analyis ################
os.system('python qpoint_xray4ota.py')
os.system('python offset_xray4ota.py')
os.system('python icmr_xray4ota.py')

################################# xraty for Ac analyis ################
os.system('python dmgain_xray4ota.py')
os.system('python cmgain_xray4ota.py')
os.system('python psneggain_xray4ota.py')
os.system('python psposgain_xray4ota.py')
os.system('python ionoise_xray4ota.py')
################################# xraty for Tran analyis ################
os.system('python slewrate_xray4ota.py')
os.system('python  thdsin_xray4ota.py')
################################# xraty for Monte-Carlo ################
os.system('python acdmmc_xray4ota.py')
#os.system('python acdmmc_readraw.py')
########################################## DC Q-operating point#################################
with open("dc/op/00000/iota.txt", "r") as file:
    iota=file.read().splitlines()
    print(iota) 
with open("dc/icmr/00000/vimin.txt", "r") as file:
    vimin=file.read().splitlines()
    print(vimin)    
##########################################  DC Offset #################################
with open("dc/offset/00000/offset.txt", "r") as file:
    offset=file.read().splitlines()
    print(offset) 
##########################################  AC analysis  (diff mode gain ) #################################
with open("ac/dm/00000/dmgain.txt", "r") as file:
    dmgain=file.read().splitlines()
    print(dmgain) 

##########################################  AC analysis  (common mode gain) #################################
with open("ac/cm/00000/cmgain.txt", "r") as file:
    cmgain=file.read().splitlines()
    print(cmgain) 


##########################################  AC analysis  (PSPOS) #################################
with open("ac/pspos/00000/pspos.txt", "r") as file:
    pspos=file.read().splitlines()
    print(pspos) 
#########################################  AC analysis  (PSneg) #################################
with open("ac/psneg/00000/psneg.txt", "r") as file:
    psneg=file.read().splitlines()
    print(psneg)    

#########################################  AC analysis  (ONOISE) #################################
with open("ac/noise/00000/inoise.txt", "r") as file:
    inoise=file.read().splitlines()
    print(inoise)    

#########################################  slew rate #################################
with open("tran/sr/00000/sr.txt", "r") as file:
    sr=file.read().splitlines()
    print(sr)    
#########################################  THD #################################
with open("tran/thd/00000/thd.txt", "r") as file:
    thd=file.read().splitlines()
    print(thd)    

#########################################  Monte carlo for AC analysis (Open loop gain) #################################
with open("ac/dmmc/00000/mcav.txt", "r") as file:
    mcav=file.read().splitlines()
    print(mcav)    


#########################################  Monte carlo for AC analysis (Gain Bandwidth, and phase margin) #################################
with open("ac/dmmc/00000/mcgbw.txt", "r") as file:
    mcgbw=file.read().splitlines()
    print(mcgbw)  


#########################################  Monte carlo for AC analysis (phase margin) #################################
with open("ac/dmmc/00000/mcpm.txt", "r") as file:
    mcpm=file.read().splitlines()
    print(mcpm)  

       
########################################################## OTA Summary Creation ####################
Summary = open("summary/OTA_Description_"+name_stru,"w")
Summary.write("\n############################### DC Q-operating point\n")

Summary.write("Total Current (A)            :   "+str(iota[0])+"\n")
Summary.write("Total Power (W)              :   "+str(iota[1]))

Summary.write("\n############################### Offset \n")
Summary.write("Offset(V)                    :   "+offset[0]+"\n")

Summary.write("\n############################### Vin_min \n")
Summary.write("Vin_min(V)                   :   "+vimin[0]+"\n")

Summary.write("\n############################### Ac analysis (diff mode gain ) \n")
Summary.write("Dc-Gain(dB)                  :   "+dmgain[0]+"\n")
Summary.write("Gain Bandwidth Product (Hz)  :   "+dmgain[1]+"\n")
Summary.write("Phase Margin (Deg)           :   "+dmgain[2]+"\n")
Summary.write("Bandwidth (Hz)               :   "+dmgain[3]+"\n")

Summary.write("\n############################### Ac analysis (common mode gain ) \n")
Summary.write("Common Mode Gain (dB)        :   "+cmgain[0]+"\n")
Summary.write("CMRR (dB)                    :   "+str(float(dmgain[0])-float(cmgain[0]))+"\n")
Summary.write("\n############################### Ac analysis (power supply rejection +ve )\n")
Summary.write("PSR+  (dB)                   :   "+pspos[0]+"\n")
Summary.write("PSRR+ (dB)                   :   "+str(float(dmgain[0])-float(pspos[0]))+"\n")

Summary.write("\n############################### Ac analysis (power supply rejection -ve )\n")
Summary.write("PSR- (dB)                    :   "+psneg[0]+"\n")
Summary.write("PSRR- (dB)                   :   "+str(float(dmgain[0])-float(psneg[0]))+"\n")


Summary.write("\n############################### Ac analysis (input reffered noise ) \n")
Summary.write("Total Input Refered Noise (V):   "+inoise[0]+"\n")
Summary.write("Over Operating Frequency     :   "+inoise[1]+"\n")

Summary.write("\n############################### slew rate \n")
Summary.write("Slew Rate (V/sec)            :   "+sr[0]+"\n")

Summary.write("\n############################### THD \n")
Summary.write("Total Harmonic Distortion (%):   "+thd[0]+"\n")
Summary.write("@ Peak Voltage (V)           :   "+thd[1]+"\n")
Summary.write("@ Operating Frequency  (Hz)  :   "+thd[2]+"\n")

Summary.write("\n############################### Monte carlo of Dc-gain (AV) \n")
Summary.write("# run of AV        :   "+mcav[0]+"\n")
Summary.write("Mean               :   "+mcav[1]+"\n")
Summary.write("Standard Deviation :   "+mcav[2]+"\n")
Summary.write("CP                 :   "+mcav[3]+"\n")
Summary.write("CPK                :   "+mcav[4]+"\n")

Summary.write("\n############################### Monte carlo of Gain BandWidth Product (GBW) \n")
Summary.write("# run of GBW       :   "+mcgbw[0]+"\n")
Summary.write("Mean               :   "+mcgbw[1]+"\n")
Summary.write("Standard Deviation :   "+mcgbw[2]+"\n")
Summary.write("CP                 :   "+mcgbw[3]+"\n")
Summary.write("CPK                :   "+mcgbw[4]+"\n")

Summary.write("\n############################### Monte carlo of Phase Margin (PM) \n")
Summary.write("# run of PM        :   "+mcpm[0]+"\n")
Summary.write("Mean               :   "+mcpm[1]+"\n")
Summary.write("Standard Deviation :   "+mcpm[2]+"\n")
Summary.write("CP                 :   "+mcpm[3]+"\n")
Summary.write("CPK                :   "+mcpm[4]+"\n")


Summary.write("\n############################### Cost Evaluation (FOM) \n")
FOM1="{:.2e}".format(cl*float(sr[0])/(float(iota[1])))
FOM2="{:.2e}".format(cl*float(dmgain[1])/(float(iota[1])))
Summary.write("FOM1=Cl*SR/Pd  (f.v/s.w)    :   "+str(FOM1)+"\n")
Summary.write("FOM2=Cl*GBW/Pd (f.Hz/w)     :   "+str(FOM2)+"\n")

Summary.close()


  