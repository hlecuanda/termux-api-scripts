# vim: number nowrap

from time import sleep
import click
import subprocess
import time

COUNTDOWN='500'
DESTINATION=''
@click.command()
@click.argument('DESTINATON', help='number to send sms to' )
@click.argument('LAPSE', help='number of repetitions')
@click.argument('COUNTDOWN', help='seconds for each repetition')
def sms(DESTINATION,COUNTDOWN,LAPSE):
    ''' periodically sends an sms message to a number '''
    
    for lap in range(1,LAPSE):    
        time.sleep(1)
        smscontent: "washusi eashuwa"
        subprocess.popen('termux-sms-send','-n',DESTINATION, smscontent)
        print('       {}  '.format(COUNTDOWN)) 
        COUNTDOWN =-1

if __name__ == "__main__":
    sms()
