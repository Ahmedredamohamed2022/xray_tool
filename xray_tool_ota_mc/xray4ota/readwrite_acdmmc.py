#!/usr/bin/env python3
import os




with open("template_tb/acdmmc_tb.spice", "r") as file:
    acdmmc_tb=file.read().splitlines()
    
with open("cut/ndiff-ota-circuit.spice", "r") as file:
    netlist_xschem=file.read().splitlines()
    
directory= os.getcwd()
print(directory)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
Summary = open("spice/acdmmc.spice","w")
for i in range(len(acdmmc_tb)):
    if(i==45):
        string = acdmmc_tb[i]
        L1=string.replace("write "+string,directory+"/ac/dmmc/rawfiles/dmmc{$&run}.raw" )
        Summary.write(L1)
        Summary.write("\n")

    else:
        st= "x is greater than y"
        Summary.write(acdmmc_tb[i])
        Summary.write("\n")


for i in range(len(netlist_xschem)-1):
    if(i==2):
        string = netlist_xschem[i]
        L1=string.replace(string, ".subckt ndiff-ota-circuit  vout vdd vss ibiasn vip vin")
        Summary.write(L1)
        Summary.write("\n")

    else:
        st= "x is greater than y"
        string = netlist_xschem[i]
        L1=string.replace("$", "${")
        string=L1.replace("@", "}")
        Summary.write(string)
        Summary.write("\n")
#string = "'"+netlist_xschem[4]+"'"
#string = netlist_xschem[4]

#print (string)
#L1=string.replace("$", "${")
#string=L1.replace("@", "}")
#print (string)


Summary.close()
