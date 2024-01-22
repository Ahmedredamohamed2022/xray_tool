#!/usr/bin/env python3
import os

directory= os.getcwd()
print(directory)
path1= directory+'/spice'

try: 
    os.mkdir(path1)

except OSError as error: 
    print(error)  

with open("template_tb/qpoint_tb.spice", "r") as file:
    qpoint_tb=file.read().splitlines()
    
with open("cut/ndiff-ota-circuit.spice", "r") as file:
    netlist_xschem=file.read().splitlines()
    


directory= os.getcwd()
print(directory)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
Summary = open("spice/qpoint.spice","w")
for i in range(len(qpoint_tb)):
    if(i==33):
        string = qpoint_tb[i]
        L1=string.replace("write "+string,directory+"/dc/op/rawfiles/dcop.raw" )
        Summary.write(L1)
        Summary.write("\n")

    else:
        st= "x is greater than y"
        Summary.write(qpoint_tb[i])
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


Summary.close()
