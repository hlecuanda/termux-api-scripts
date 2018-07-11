#!/usr/bin/env python
# vim: number nowrap

from time import sleep
import click
import subprocess
import time

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
def sms():
    pass

@click.command('periodic', short_help='repeat message periodically')
@click.argument('DESTINATON')
@click.argument('LAPSE')
@click.argument('COUNTDOWN')
def periodic(DESTINATION,COUNTDOWN,LAPSE):
    ''' periodically sends an sms message to a number '''
    
    for lap in range(1,LAPSE):    
        time.sleep(1)
        smscontent: "washusi eashuwa"
        subprocess.popen('termux-sms-send','-n',DESTINATION, smscontent)
        print('       {}  '.format(COUNTDOWN)) 
        COUNTDOWN =-1
