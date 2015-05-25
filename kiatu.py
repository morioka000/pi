import pexpect
import sys
import time


bluetooth_adr = sys.argv[1]
tool = pexpect.spawn('gatttool -b ' + bluetooth_adr + ' --interactive')
tool.expect('\[LE\]>')
print "Preparing to connect. You might need to press the side button..."
tool.sendline('connect')

tool.sendline('char-write-cmd 0x4f 01')
tool.expect('\[LE\]>')
tool.sendline('char-read-hnd 0x4b')
tool.expect('descriptor: .*')
rval = tool.after.split()
print rval

tool.expect('\[LE\]>')    
tool.sendline('char-read-hnd 0x52')
tool.expect('descriptor: .*')
rval0 = tool.after.split()
print rval0
sys.exit()



c1=floatfromhex(rval[2] + rval[1])
c2=floatfromhex(rval[4] + rval[3])
c3=floatfromhex(rval[6] + rval[5])
c4=floatfromhex(rval[8] + rval[7])
c5=floatfromhex(rval[10] + rval[9])
c6=floatfromhex(rval[12] + rval[11])
c7=floatfromhex(rval[14] + rval[13])
c8=floatfromhex(rval[16] + rval[15])


Sensitivity = (c3 + ((c4 * Temp) / 2^17) + ((c5 * Temp^2) / 2^34))
Offset = (c6 * 2^14) + ((c7 * Temp) / 2^3) + ((c8 * Temp^2) / 2^19)
Pa = (Sensitivity * press + Offset) / 2^14