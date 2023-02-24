Probably, Direct Kernel Object Manipulation (DKOM) attack


########################################

# 1 - 7

vol.py -f banking-malware.vmem kdbgscan
vol.py -f banking-malware.vmem imageinfo
vol.py -f banking-malware.vmem  --profile=Win7SP1x64_24000 psxview
vol.py -f banking-malware.vmem  --profile=Win7SP1x64_24000 diilist --offset=0x000000007d336950
vol.py -f banking-malware.vmem --profile=Win7SP1x64_24000 procdump --offset=0x000000007d336950 --dump-dir=/cases/my/78/output
vol.py -f banking-malware.vmem --profile=Win7SP1x64_24000 malfind --offset=0x000000007d336950
vol.py -f banking-malware.vmem --profile=Win7SP1x64_24000 vadinfo --offset=0x000000007d336950
cat vadinfo_0x000000007d336950.txt | grep VAD | grep -E "220000|2a10000|2a80000" | awk -F ' ' '{printf("%s %s\n", $8, $6)}' | while read l; do a=($l); end=${a[0]}; start=${a[1]}; size=$((end-start)); echo $end - $start = `printf '%X\n' $size`; done

########################################

# 8
## volatility2
### simple
vol -f banking-malware.vmem --profile Win7SP1x64_24000 volshell
cc(offset=0x000000007d336950, physical=True)
sc()
proc()
type(proc())
proc().ExceptionPortData ... test
proc().ActiveProcessLinks
type(proc().ActiveProcessLinks)
proc().ActiveProcessLinks.Blink ... test
proc().ActiveProcessLinks.Flink
type(proc().ActiveProcessLinks.Flink)
cc(offset=0xFFFFFA800397DC88 - 0x188, physical=False)
####J dumn calc
echo $((0xFFFFFA800397DC88 - 0x188)) | xargs printf "%x\n"
cc(offset=0xfffffa800397db00, physical=False)

### another
for v_addr in self.getpidlist():
	cc(offset=str(v_addr))
	print "ActiveProcessAddr = ", proc().ActiveProcessLinks
	print "Flink = ", hex(proc().ActiveProcessLinks.Flink)
	print "Blink = ", hex(proc().ActiveProcessLinks.Blink)

cat volshell_FBlist.txt | grep -i -B 5 0xFFFFFA80045FC568

## volatility3 ... Noooo, especially a pyhsical address
volshell3 -f banking-malware.vmem -w
for p in ps():
	i

########################################

#9
vol -f banking-malware.vmem --profile Win7SP1x64_24000 volshell
dt("OBJECT_HEADER", 0x000000007d336950-0x30, space=addrspace().base) ... space!
dt("_POOL_HEADER" ,0x000000007d336950-0x60, space=addrspace().base)
printf '%X\n' 1416573010 | xxd -r -p && echo '' ... incorrect answer
printf '%X\n' 1416573010 | xargs echo | fold -w2 | /bin/tac | tr -d '\n' | xxd -r -p && echo '' ... from LittleEndian to BigEndian

##
Above, I converted the value from decimal to hexadecimal format, swapped the bytes (because in memory the value is located from low to high bytes, that is, I brought it from LittleEndian to BigEndian format) and converted to char. The output was " R0ot ".
##


########################################

# 10
dt("_POOL_HEADER" ,0x000000007d336950-0x60, space=addrspace().base)
hex(0x7D3368F0 + 0x4)
