# vim: number nowrap

from time import sleep
import click
import subprocess
import time

COUNTDOWN='500'
DESTINATION=''
@click.command()
@click.option()
def sms():
    ''' periodically sends an sms message to a number '''
    while True:
        time.sleep(1)
        smscontent: "washusi eashuwa"
        subprocess.popen('termux-sms-send','-n',DESTINATION, smscontent)
        print('       {}  '.format(COUNTDOWN)) 
        countdown =-1

if __name__ == "__main__":
    sms()
