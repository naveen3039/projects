#!/usr/bin/python3.8
############# Script Details #################################################################

# Script Name            :  test_googledrive.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  23-06-21
# last_modification_date :  25-06-21

##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed such that test on for the all the operations
# like COPY, CREATE, DELETE, EMPTYTRASH, EXPORT, GET, LIST and UPDATE on Googledrive_api

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Created a Google_drive api with Object-Oriented Programming.

# 2.Given respective credentials and permissions to it.

# 3.Testing various method of copy, create, delete, emptytrash, export, get, list and update 
#   with different test cases

# 4.A log file created with the current date time along with message specified.

# 5.Created Custom Exception for erroneous conditions

######################################################################################################
# Importing required modules for the Script.
import sys
#Setting path for import from common modules
sys.path.append('/home/infinite/Documents/code/ubuntu/task/google_drive/common_modules')

from google_drive_api import (Googledrive,Noelements)
import pytest
import os
import logging

#Seted path for capture live loggers
pytest.main(args=["-sv", os.path.abspath(__file__)]) 

#Fixing google drive configuration testing their methods
@pytest.fixture
def drive():
    config = Googledrive()
    logging.info("Intialised Googledrive")
    return config

#Testing file was inside a folder or not
def test_file_in_folder(drive):
    try:
        file_id=drive.file_in_folder('quickstart.py','/home/infinite/Documents/code/ubuntu/task/google_drive/prerequistes/quick_start.py','text/python')
        assert len(file_id) != 0 , 'File was not present' 
        logging.info('Checking file present in inside folder')
        lists=drive.list_file("'methods.py'")
        for list in lists:
            if file_id == list['id']:
                logging.info('file was present in folder')
                assert file_id == list['id'],'The file is not in folder'
                assert list['name'] == 'quickstart.py', 'The file is not there in folder'
    except Exception as f:
        logging.info(f)

#Testing file was inside a folder or not with negative cases
def test_file_in_folder_negative(drive):
    try:
        file_id=drive.file_in_folder('quickstart.py','/home/infinite/Documents/code/ubuntu/task/google_drive/prerequistes/quick_start.py','text/python')
        assert len(file_id) == 0 , 'File was not present' 
        logging.info('Checking file present in inside folder')
        lists=drive.list_file("'methods.py'")
        for list in lists:
            if file_id == list['id']:
                logging.info('file was present in folder')
                assert file_id != list['id'],'The file is not in folder'
                assert list['name'] != 'quickstart.py', 'The file is not there in folder'
    except Exception as f:
        logging.info(f)


#Testing file upload in drive or not
def test_upload(drive):
    try:
        fileid = drive.uploadFile('quickstart.py','/home/infinite/Documents/code/ubuntu/task/google_drive/prerequistes/quick_start.py','text/python')
        assert len(fileid) != 0 , 'File was not present' 
        logging.info('Checking file present in drive or not')
        lists=drive.list_file("'quickstart.py'")
        for list in lists:
            if fileid == list['id']:
                logging.info('file uploaded')
                assert fileid == list['id'],'The file is not in drive'
                assert list['name'] == 'quickstart.py', 'The file was not uploaded'
    except Exception as f:
        logging.info(f)

#Testing file upload in drive or not with negative test cases
def test_upload_negative(drive):
    try:
        fileid = drive.uploadFile('quickstart.py','/home/infinite/Documents/code/ubuntu/task/google_drive/prerequistes/quick_start.py','text/python')
        assert len(fileid) != 0 , 'File was not present' 
        logging.info('Checking file present in drive or not')
        lists=drive.list_file("'quickstart.py'")
        for list in lists:
            if fileid == list['id']:
                logging.info('file uploaded')
                assert fileid != list['id'],'The file is not in drive'
                assert list['name'] != 'quickstart.py', 'The file was not uploaded'
    except Exception as f:
        logging.info(f)


#Testing folder created in drive or not
def test_createFolder(drive):
    try:
        folderid = drive.createFolder('testing1')
        assert len(folderid) != 0 , 'Folder was not present' 
        logging.info('Checking Folder present in drive or not')   
        drivefolders=drive.list_file("'test'") 
        for folder in drivefolders:
            if folderid == folder['id']:
                logging.info('folder Created')
                assert folderid == folder['id'],'The folder is not in drive'
                assert folder['name'] == 'test', 'The folder was not uploaded'
    except Exception as f:
        logging.info(f)

#Testing folder created in drive or not with negative test cases
def test_createFolder_negative(drive):
    try:
        folderid = drive.createFolder('testing1')
        assert len(folderid) != 0 , 'Folder was not present' 
        logging.info('Checking Folder present in drive or not')   
        drivefolders=drive.list_file("'test'") 
        for folder in drivefolders:
            if folderid == folder['id']:
                logging.info('folder Created')
                assert folderid != folder['id'],'The folder is not in drive'
                assert folder['name'] != 'test', 'The folder was not uploaded'
    except Exception as f:
        logging.info(f)

#Testing list of files  getting or not
def test_list_files(drive):
    try:
        lists =drive.list_files()
        assert len(lists) != 0,'No files are present'
        logging.info('Files is present')
    except Exception as f:
        logging.info(f)

#Testing list of files getting or not with negative test cases
def test_list_files_negative(drive):
    try:
        lists =drive.list_files()
        assert len(lists) == 0,'No files are present' 
    except Exception as f:
        logging.info(f)

#Testing list of files with a specific name getting or not
def test_list_file(drive):
    try:
        lists = drive.list_file("'quickstart.py'")
        assert len(lists) != 0 
        assert type(lists) == list
        logging.info('Drive contains list of files')
    except Exception as f:
        logging.info(f)

#Testing list of files with a specific name getting or not with negative test cases
def test_list_file_negative(drive):
    try:
        lists = drive.list_file("'quickstart.py'")
        assert len(lists) == 0 
        assert type(lists) != list
        logging.info('Drive contains list of files')
    except Exception as f:
        logging.info(f)


#Testing list of files getting or not
def test_get_file(drive):
    try:
        id='15d7beo2pxw-eoZG9XPBwVJmoYstpGcLI'
        properties = drive.get_file(id)
        assert len(properties) != 0
        assert len(properties) >= 0
        assert type(properties) == dict
        assert properties['id'] == id
    except Exception as f:
        logging.info(f)



#Testing list of files getting or not with negative test cases
def test_get_file_negative(drive):
    try:
        id='15d7beo2pxw-eoZG9XPBwVJmoYstpGcLI'
        properties = drive.get_file(id)
        assert len(properties) == 0
        assert len(properties) <= 0
        assert type(properties) != dict
        assert properties['id'] != id
    except Exception as f:
        logging.info(f)


#Testing copy of files working or not
def test_copy_file(drive):
    try:
        id='1yM8Ie7OcSWrSBOzPajuuvfBmrqU8n3cO'
        copy=drive.copy_file(id)
        assert id != copy
        lists = drive.list_file("'methods.py'")
        for list in lists:
            if copy == list['id']:
                logging.info('file uploaded')
                assert copy == list['id'],'The file is not in drive'
                assert list['name'] == 'methods.py', 'The file was not copied'
    except Exception as f:
        logging.info(f)

#Testing copy of files working or not with negative test cases
def test_copy_file_negative(drive):
    try:
        id='1yM8Ie7OcSWrSBOzPajuuvfBmrqU8n3cO'
        copy=drive.copy_file(id)
        assert id != copy
        lists = drive.list_file("'methods.py'")
        for list in lists:
            if copy == list['id']:
                logging.info('file uploaded')
                assert copy != list['id'],'The file is not in drive'
                assert list['name'] != 'methods.py', 'The file was not copied'
    except Exception as f:
        logging.info(f)


#Testing deletion of files working or not
def test_delete_file(drive):
    id='1wBM3DvrgXusiO4KDVwNA_RFFd8RKDUYy'
    with pytest.raises(Noelements) as err_info:
        drive.delete_file(id)
    logging.info(str(err_info))
    logging.info("The file is  deleted")


#Tesing trashbox is empty or not
def test_emptyTrash(drive):
    try:
        results = drive.empty_trash()
        assert results == '','it is not a empty trash box'
        logging.info('It is a empty trash box ')
    except Exception as f :
        logging.info(f)


#Tesing trashbox is empty or not with negative test cases
def test_emptyTrash_delete(drive):
    try:
        results = drive.empty_trash()
        assert results != '','it is not a empty trash box'
        logging.info('It is a empty trash box ')
    except Exception as f :
        logging.info(f)     


#Testing exporting contents of doc file or not
def test_export(drive):
    try:
        id='1HBB7LUXxAHV4GXVQQGI6WTU9nZmP_APAUP0Xg2PsD14'
        results = drive.export(id)
        logging.info(results)
        assert len(results) != 0 ,'The results was not exported'
        assert results != None,'The results was not exported'
    except Exception as f:
        logging.info(f)

#Testing exporting contents of doc file or not with negative testcases
def test_export_negative(drive):
    try:
        id='1HBB7LUXxAHV4GXVQQGI6WTU9nZmP_APAUP0Xg2PsD14'
        results = drive.export(id)
        logging.info(results)
        assert len(results) == 0 ,'The results was not exported'
        assert results == None,'The results was not exported'
    except Exception as f:
        logging.info(f)

#Testing Generating ids or not
def test_generateids(drive):
    try:
        results=drive.generate_id()
        assert len(results) != 0,'ids was not generated'
        assert type(results) == dict ,'type of results are differnt'
        logging.info('Generated ids sucessfully')
    except Exception as f:
        logging.info(f)

#Testing Generating ids or not with negative text cases
def test_generateids_negative(drive):
    try:
        results=drive.generate_id()
        assert len(results) == 0,'ids was not generated'
        assert type(results) != dict ,'type of results are differnt'
        logging.info('Generated ids sucessfully')
    except Exception as f:
        logging.info(f)



#Testing file moving or not 
def test_movefile(drive):
    try:
        file_id = '1yM8Ie7OcSWrSBOzPajuuvfBmrqU8n3cO'
        folder_id = '1BSzgK0JboG1db6EueiPjXLWykopztmHE'
        results =  drive.move_file(file_id,folder_id) 
        assert results['id'] == file_id ,'file was not found'
        assert results['parents']==[folder_id],'folder was not found'
        logging.info(f'The file is sucessfully move to folder containg id:{folder_id} ')
    except Exception as f:
        logging.info(f)


#Testing file moving or not with negative testcases
def test_movefile_negative(drive):
    try:
        file_id = '1yM8Ie7OcSWrSBOzPajuuvfBmrqU8n3cO'
        folder_id = '1BSzgK0JboG1db6EueiPjXLWykopztmHE'
        results =  drive.move_file(file_id,folder_id) 
        assert results['id'] != file_id ,'file was not found'
        assert results['parents'] != [folder_id],'folder was not found'
        logging.info(f'The file is sucessfully move to folder containg id:{folder_id} ')
    except Exception as f:
        logging.info(f)




