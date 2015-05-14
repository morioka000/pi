import pexpect #コマンドラインをプログラムで実行するためのライブラリ
import sys
import time

def floatfromhex(h):#バグらないように？
    t = float.fromhex(h)
    if t > float.fromhex('7FFF'):
        t = -(float.fromhex('FFFF') - t)
        pass
    return t


def calchumTarget(temp,hum):#湿度計算関数(tempが温度,jumが湿度)
    v0=-46.85+175.72/65536*temp;#vが温度
    v1=-6.0 + 125.0/65536 * v0;#v1が湿度
    print "%.2f C" % v1


bluetooth_adr = sys.argv[1]#デバイスのMACアドレス
tool = pexpect.spawn('gatttool -b ' + bluetooth_adr + ' --interactive')
tool.expect('\[LE\]>')
print "Preparing to connect. You might need to press the side button..."
tool.sendline('connect')
tool.sendline('char-write-cmd 0x29 01')
tool.expect('\[LE\]>')
    tool.sendline('char-read-hnd 0x25')
    tool.expect('descriptor: .*')
    rval = tool.after.split()#区切り毎に配列に生データを格納？
    Temp = floatfromhex(rval[2] + rval[1])#計算用変数に数値を格納
    Hum = floatfromhex(rval[4] + rval[3])
    #print rval
    calcTmpTarget(Temp,Hum)
sys.exit()
