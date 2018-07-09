# vim: number nowrap

from time import sleep
import subprocess
import time

COUNTDOWN='500'
DESTINATION='6461508444'
while True:
    time.sleep(1)
    smscontent: "washusi eashuwa"
    subprocess.popen('termux-sms-send','-n',DESTINATION, smscontent)
    print('       {}  '.format(COUNTDOWN)) 
    countdown =-1


