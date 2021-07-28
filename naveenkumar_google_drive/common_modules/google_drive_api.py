#!/usr/bin/python3.8
############# Script Details #################################################################

# Script Name            :  google_drive_api.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  23-06-21
# last_modification_date :  25-06-21

##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed such that work on for the all the operations
# like COPY, CREATE, DELETE, EMPTYTRASH, EXPORT, GET, LIST and UPDATE on Googledrive_api

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Created a Google_drive api with Object-Oriented Programming.

# 2.Given respective credentials and permissions to it.

# 3.Created various methods of copy, create, delete, emptytrash, export, get, list and update

# 4.A log file created with the current date time along with message specified.

# 5.Created Custom Exception for erroneous conditions

######################################################################################################
# Importing required modules for the Script.
import sys

#Setting path for import from drive from quickstart
sys.path.append('/home/infinite/Documents/code/ubuntu/task/google_drive/prerequistes')

from quick_start import main
from apiclient.http import MediaFileUpload
from error import Noelements
import logging



# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="drive.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO,
)

class Googledrive:
    '''Creating a class of Googledrive'''
    logging.info('Created a class of google drive')
    
    def __init__(self):
        '''Intialising Google drive'''
        self.service=main()
        logging.info('configured to google drive')

    def file_in_folder(self,filename,filepath,mimetype):
        '''Creating a file in folder'''
        folder_id='1BSzgK0JboG1db6EueiPjXLWykopztmHE'
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        #Mediafileupload function helps to upload file
        media = MediaFileUpload(filepath,
                                mimetype=mimetype,
                                resumable=True)
        #File upload in folder with create method
        try:
            file = self.service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id').execute()
            logging.info('File ID: %s' % file.get('id'))
            logging.info('File created inside a folder')
            return file.get('id')
        except:
            logging.info(f'There is no such folder containing {folder_id}')
            raise Noelements(f'There is no such folder containing {folder_id}')



    def uploadFile(self,filename,filepath,mimetype):
        '''Upload a file'''
        file_metadata = {'name': filename}
        #Mediafileupload function helps to upload file
        media = MediaFileUpload(filepath,
                                mimetype=mimetype)
        try:
            #File upload in drive with create method
            file = self.service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id').execute()
            logging.info('File ID: %s' % file.get('id'))
            logging.info(f'{filename} file sucessfully uploaded')
            return file.get('id')
        except:
            logging.info('failed to upload a file')
            raise Noelements(f'failed to upload a file')


    def createFolder(self,name):
        '''Creating a folder in drive '''
        file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
        }
        try:
            #Folder Created in drive with create method
            file = self.service.files().create(body=file_metadata,
                                                fields='id').execute()
            logging.info('Folder ID: %s' % file.get('id'))
            logging.info(f'{name} folder was created in drive')
            return file.get('id')
        except:
            logging.info('failed to upload a folder')
            raise Noelements(f'failed to upload a folder')

    def list_file(self,name):
        '''List all files with such name '''
        try:
            #list all files with such name using list method
            results = self.service.files().list(q=f"name={name}",
            fields="nextPageToken , files(id, name)").execute()
            items = results.get('files', [])
            if not items:
                logging.info('No files found.')
            else:
                logging.info('Getting list of files')
            return items
        except:
            logging.info(f'There is no such file as {name}')
            raise Noelements(f'There is no such file {name}')

    def list_files(self):
        '''list all files in drive'''
        try:
            #list all files in drive using list method
            results = self.service.files().list(
            fields="nextPageToken , files(id, name)").execute()
            items = results.get('files', [])
            if not items:
                logging.info('No files found.')
            else:
                logging.info('getting list of Files:')
            return items
        except:
            logging.info(f'No Files are present')
            raise Noelements(f'No files are present') 


    def get_file(self,id):
        '''Getting a specific file properties'''
        try:
            #Get a specific file properties with get method
            results = self.service.files().get(fileId=id).execute()
            logging.info(results)
            return results
        except:
            logging.info(f'No File are present with such a file id {id}')
            raise Noelements(f'No file are present with such a file id {id}')
    
    
    def copy_file(self,id):
        '''Coping a file'''
        try:
            #Copying a specific file with copy method
            results = self.service.files().copy(fileId=id).execute()
            logging.info(results)
            return results 
        except:
            logging.info(f'No File are present with such a file id {id}')
            raise Noelements(f'No file are present with such a file id {id}')

    def delete_file(self,id):
        '''Deleting a file'''
        try:
            #Deleting a specific file with delete method
            results = self.service.files().delete(fileId=id).execute()
            logging.info('Deleted a specific file')
            return "deleted"
        except:
            logging.info(f'No File are present with such a file id {id}')
            raise Noelements(f'No file are present with such a file id {id}')
            
    
    def empty_trash(self):
        '''Deleting all files are in trash'''
        #Deleting files using emptyTrash method
        results = self.service.files().emptyTrash().execute()
        logging.info(results)
        return results

    def export(self,id):
        '''Export conents of doc file'''
        try:
            #Exporting conents of doc file with export
            results = self.service.files().export(fileId=id,mimeType='text/plain').execute()
            logging.info(results)
            return results
        except:
            logging.info(f'No File are present with such a file id {id}')
            raise Noelements(f'No file are present with such a file id {id}')


    def generate_id(self):
        '''Generates a set of file IDs which can be provided in create or copy requests '''
        try:
            #Genrating ids using generateids method
            results = self.service.files().generateIds().execute()
            logging.info(results)
            return results
        except:
            logging.info(f'No ids are generated')
            raise Noelements(f'No ids are generated')


    def move_file(self,file_id,folder_id):
        '''Moving a file to a folder with update method'''
        try:
            # Retrieve the existing parents to remove
            file = self.service.files().get(fileId=file_id,
                                            fields='parents').execute()
            previous_parents = ",".join(file.get('parents'))
            # Move the file to the new folder 
            file = self.service.files().update(fileId=file_id,
                                            addParents=folder_id,
                                            removeParents=previous_parents,
                                            fields='id, parents').execute()  
            return file
        except:
            logging.info(f'No File are present with such a file id {id}')
            raise Noelements(f'No file are present with such a file id {id}')
           

                                                 