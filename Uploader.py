# vim: number nowrap : 
# coding: utf-8

def installreqs():
    REQ=['google-auth','google-auth-httplib2','google-api-python-client','oauth2client','gaesd','PyDrive']
    for module in REQ:
        print('installing module {}'.format(module))
        cmd= 'pip -q install {}'.format(module)
        get_ipython().system(cmd)   

try:
    import pydrive
    from google.oauth2 import service_account
    from oauth2client.service_account import ServiceAccountCredentials
except ModuleNotFoundError:
    installreqs()
else:
    print('all dependencies installes already')
finally:
    import re
    import os.path  
    import sys
    import httplib2
    from pydrive.drive import GoogleDrive
    from apiclient import discovery
    from google.oauth2 import service_account
    from oauth2client.service_account import ServiceAccountCredentials

SERVICE_ACCOUNT_FILE = './MezaOps-9483d786f5ef.json'
DEVEL=True
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive.metadata.readonly']

with open(SERVICE_ACCOUNT_FILE, "r") as f:
    print('loaded credentials from {}'.format(f.name))

credentials = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

delegated_credentials = credentials.create_delegated('hector@lecuanda.com')  
delegated_http = delegated_credentials.authorize(httplib2.Http())
drive  = discovery.build('drive', 'v3', http=delegated_http)
gd=GoogleDrive()                           

if DEVEL:
    dir_id = "1G6ugwhummqXDYcDVysgw_gSUdcejO4gj" # while testing
    print('Developer Test dir on gdrive')
else:
    dir_id = "104tvKpVICsqcdZ5vEM9Ioc-Bi0U8XNPj" # Live
    print('live dir ong Gdrive')
    
d=os.path.relpath(start='.',path='../../../Call Recorder')
os.chdir(d)

def upload_to_dir(src,dest_dir=dir_id):
    f=gd.CreateFile()
    f['title']=src
    f.Upload(param={'http':delegated_http})
    


    
