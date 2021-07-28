############# Script Details #################################################################

# Script Name            :  naveen_kumar_test_gmail.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  27-05-21
# last_modification_date :  27-05-21

##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed such that test delete ,access, modify ,trash the emails

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Created a gmail api .

# 2.Given respective credentials and permissions to it.

# 3.Created various method of delete ,access,modify,trash and tested with tested cases 

# 4.A log file created with the current date time along with message specified.

##############################################################################################

from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pytest
import logging

# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="todo.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO,
    )



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']


"""Shows basic usage of the Gmail API.
Lists the user's Gmail labels.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)
logging.info("build api for gmail with credentials")

def test_get_id():
# Accessing msg id of the emails
    results = service.users().messages().list(userId='me',maxResults=1).execute()
    results.get('messages', [])
    logging.info("accessed msg id of the emails")
    assert type(results.get('messages', [])) == list
    
def test_get_msg():
# Accessing msg with id of the emails
    results = service.users().messages().list(userId='me',maxResults=1).execute()
    ids=results.get('messages', [])
    logging.info("accessed msg with id of the emails")
    for i in ids:
        results = service.users().messages().get(userId='me',id=i['id']).execute()
        assert results != None


def test_modify():
#Modifiying the labels
   results = service.users().messages().list(userId='me',maxResults=1).execute()
   ids=results.get('messages', [])
   logging.info("modified the labels")
   for msg_id in ids:
     body1={"addLabelIds":["INBOX"],"removeLabelIds":["CATEGORY_UPDATES"]}
     data=service.users().messages().modify(userId='me',id=msg_id['id'],body=body1).execute()
     assert "INBOX" in data['labelIds'] 
     assert "CATEGORY_UPDATES" not  in data['labelIds'] 
     
     
def test_trash():
#Sending to trash with respective message id
      results= service.users().messages().trash(userId='me',id='179acfc1588566f1').execute()
      logging.info("message sented to trash")
      result = service.users().messages().list(userId='me').execute()
      ids=result.get('messages', [])
      for i in ids:
          assert i['id'] != '179acfc1588566f1'

def test_untrash():
#Untrashing message with respective message id
      results= service.users().messages().trash(userId='me',id='179acfc1588566f1').execute()
      logging.info(" untrashed message with respective message id")
      result = service.users().messages().list(userId='me').execute()
      ids=result.get('messages', [])
      for i in ids:
          assert i['id'] != '179acfc1588566f1'

def test_delete():
#Deleting message respective message id
    results= service.users().messages().delete(userId='me',id ='179acfc1588566f1').execute()
    logging.info(" deleted message with respective message id")
    result = service.users().messages().list(userId='me').execute()
    ids=result.get('messages', [])
    for i in ids:
          assert i['id'] != '179acfc1588566f1'



    
    
    



    


    

