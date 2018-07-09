#!/usr/bin/env ipython
# vim: number nowrap : 
# coding: utf-8

try:
    from oauth2client.service_account import ServiceAccountCredentials
    from google.oauth2 import service_account
    import gspread
except:
    !pip install google-auth google-auth-httplib2 google-api-python-client gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import gspread
    # from gspread.models import Cell
finally:
    import re
    import sys
    import httplib2
    from apiclient import discovery

SERVICE_ACCOUNT_FILE = 'MezaOps-9483d786f5ef.json'

SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/spreadsheets']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


delegated_credentials = credentials.create_delegated('hector@lecuanda.com')  
delegated_http = delegated_credentials.authorize(httplib2.Http())
drive  = discovery.build('drive', 'v3', http=delegated_http)


dir_id = "1kghdjPxiHRvQY2sQa1koli2csSGqni8_" #@param {type:"string"}
#drivequery="'{}' in parents and mimeType = \
'application/vnd.google-apps.document'".format(dir_id)
docs = drive.files().list(q=drivequery).execute()

print("{} documents selected".format(len(docs['files'])))
