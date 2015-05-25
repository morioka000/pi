import pexpect
import sys
import time

def floatfromhex(h):
    t = float.fromhex(h)
    if t > float.fromhex('7FFF'):
        t = -(float.fromhex('FFFF') - t)
        pass
    return t



def calcpressTarget(temp, press):
    
    tool.sendline('char-write-cmd 0x4f 01')
    tool.sendline('char-read-hnd 0x52')
    tool.expect('descriptor: .*')
    rval0 = tool.after.split()
    for x in rval0[1:8]:
        c[x]=floatfromhex(rval0[x])
    print rval0
    
    
    
    
    
    print "%.2f C" % tObj


bluetooth_adr = sys.argv[1]
tool = pexpect.spawn('gatttool -b ' + bluetooth_adr + ' --interactive')
tool.expect('\[LE\]>')
print "Preparing to connect. You might need to press the side button..."
tool.sendline('connect')
# test for success of connect
#tool.expect('\[CON\].*>')
tool.sendline('char-write-cmd 0x4f 01')
tool.expect('\[LE\]>')
tool.sendline('char-read-hnd 0x4b')
tool.expect('descriptor: .*')
rval = tool.after.split()
temp = floatfromhex(rval[2] + rval[1])
press = floatfromhex(rval[4] + rval[3])
calcpressTarget(temp, press)


sys.exit()
