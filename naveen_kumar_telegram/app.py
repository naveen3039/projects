#!/usr/bin/python3.8
############# Script Details #################################################################

# Script Name            :  app.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  27-06-21
# last_modification_date :  29-06-21

##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed such that to create a notification in Telegram App for 
# the Cloud/Virtual Box servers

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Create a telegram api to send notification

# 2.Given respective credentials and permissions to it.

# 3.Checking ping of cloud server if it is get positive response  all cpu ram details of server will be stored in a file
# sending a notification in telegram that server in on

# 3.Checking ping of cloud server if it is get negative response sending details of server file as email to admin
# sending a notification in telegram that server is down

# 4.A log file created with the current date time along with message specified.

# 5.For erroneous conditions will be stored in log file

######################################################################################################
# Importing required modules for the Script.
from ping3 import ping
import requests
import datetime
import csv
import paramiko
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
from config import (token ,chat_id, username , hostname , server_password , emailfrom ,emailto ,email_password )
import logging



# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="telegram_api.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO,
)


def ping_ip(host):
    '''This function gets server response'''
    response = ping(host)
    #Check getting response or not
    if not response :
        logging.info("SERVER IS DOWN")
        return False
    else:
        logging.info("SERVER IS ON")
        return True

token = token
chat_id= chat_id
username = username
hostname = hostname
server_password = server_password
commands = [
    "hostnamectl",
    "top -b -n1 | grep 'Cpu(s)' | awk '{print $2 + $4}' ",
    "free | grep Mem | awk '{print $4/$2 * 100.0}'"
    ]

#creating a file 
header=['Name','IP','CPU',"ram",'dateandtime']
with open('data.csv','w')as f:
    logging.info("data.csv file created")
    writer = csv.DictWriter(f,fieldnames=header)
    writer.writeheader()

try:
    #Check server is working or not
    if ping_ip(hostname) == False:
        base_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text="The server is goes down"' 
        response=requests.get(base_url) 
        logging.info(response.json())
        
        emailfrom = emailfrom
        emailto = emailto
        username =  emailfrom
        fileToSend = "data.csv"
        email_password = email_password

        msg = MIMEMultipart()
        msg["From"] = emailfrom
        msg["To"] = emailto
        msg["Subject"] = "task on cpu ram usage"
        msg.preamble = "task on cpu ram usage"

        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":
            fp = open(fileToSend)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
        msg.attach(attachment)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username,email_password)
        server.sendmail(emailfrom, emailto, msg.as_string())
        logging.info("Email sent successfully")
    
    #Check server is working or not
    if ping_ip(hostname) == True:
        base_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text="The server is working"' 
        response=requests.get(base_url) 
        logging.info(response.json())
        
        # initialize the SSH client
        client = paramiko.SSHClient()
        # add to known hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=hostname, username=username,password=server_password)
            logging.info("server connected trough ssh")
        except:
            logging.info("[!] Cannot connect to the SSH Server")
            exit()

        lst = []
        #looping commands executing in terminal
        for command in commands:
            stdin, stdout ,stderr= client.exec_command(command)
            ls = stdout.read().decode()
            lst.append(ls)
        logging.info(lst)
        header=['Name','IP','CPU',"ram",'dateandtime']
        with open('data.csv','w')as f:
            logging.info("Storing details in csv file")
            d = datetime.datetime.now()
            writer = csv.DictWriter(f,fieldnames=header)
            writer.writeheader()
            writer.writerow({'Name':username,'IP':hostname,'CPU':lst[1].split('\n')[0],"ram":lst[2].split('\n')[0],'dateandtime':"%s-%s-%s %s:%s:%s" % (d.day, d.month, d.year,d.hour, d.minute, d.second)})
except Exception as e:
    logging.info(e)

