# vim: number nowrap

import re
import sys
import time
from time import sleep
from subprocess import run
from subprocess import Popen

DESTINATION='6461508444'

def prep(content):
    p=re.compile(r'\s')
    word=p.replace(content)
    print(word)

    #smscontent: "washusi eashuwa"
    #subprocess.popen('termux-sms-send','-n',DESTINATION, smscontent)
    #print('       {}  '.format(COUNTDOWN)) 
    #countdown =-1

def main(c):
    prep(c)

if __name__ == '__main__':
    try:
        if not sys.argv[1]:
            content = 'figlet figlet'
        else:
            content = sys.argv[1:].join("_")
    except IndexError:
        content = 'figlet figlet'
main(content)



