#!/bin/bash
rund=$(readlink -f $(dirname $0))
runn=$(basename $rund)
src=tb.spi
srcp=$rund/$src
logp=$rund/run.log

# rawFile="out.raw"
rawFile="CORNERS:${CORNERS}_TEMP:${TEMP_VAL}_VDD:${VDD_VAL}_DVDD:${VDD_VAL}.raw"

echo log: $logp
echo src: $srcp
echo in dir: $rund
echo
cd $rund
echo "set ngbehavior=hsa" > .spiceinit
echo running " ngspice -b $src -r $rawFile >& $logp"
exec ngspice -b $src -r $rawFile  >& $logp
# 
