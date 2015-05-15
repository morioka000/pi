#!/usr/bin/env python
# Michael Saunby. April 2013
#
# Read temperature from the TMP006 sensor in the TI SensorTag
# It's a BLE (Bluetooth low energy) device so using gatttool to
# read and write values.
#
# Usage.
# sensortag_test.py BLUETOOTH_ADR
#
# To find the address of your SensorTag run 'sudo hcitool lescan'
# You'll need to press the side button to enable discovery.
#
# Notes.
# pexpect uses regular expression so characters that have special meaning
# in regular expressions, e.g. [ and ] must be escaped with a backslash.
#

import pexpect
import sys
import time

def floatfromhex(h):
    t = float.fromhex(h)
    if t > float.fromhex('7FFF'):
        t = -(float.fromhex('FFFF') - t)
        pass
    return t


# This algorithm borrowed from
# http://processors.wiki.ti.com/index.php/SensorTag_User_Guide#Gatt_Server
# which most likely took it from the datasheet.  I've not checked it, other
# than noted that the temperature values I got seemed reasonable.
#
def calcpressTarget(temp, press):
    
    
    
    
    
    
    
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
    tool.sendline('char-read-hnd 0x52')
    tool.expect('descriptor: .*')
    rval0 = tool.after.split()
    for x in rval0[1:8]:
        c[x]=floatfromhex(rval0[x])
    print rval
    calcpressTarget(temp, press)
sys.exit()
