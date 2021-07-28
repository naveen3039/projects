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


def ping_ip(host):
    response = ping(host)
    if not response :
        return False
    else:
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
    
if ping_ip(hostname) == False:
    base_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text="The server is goes down"' 
    response=requests.get(base_url) 
    print(response.json())
    
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
  
if ping_ip(hostname) == True:
    base_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text="The server is working"' 
    response=requests.get(base_url) 
    print(response.json())
    # initialize the SSH client
    client = paramiko.SSHClient()
    # add to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username,password=server_password)
    except:
        print("[!] Cannot connect to the SSH Server")
        exit()

    lst = []
    for command in commands:
        stdin, stdout ,stderr= client.exec_command(command)
        ls = stdout.read().decode()
        lst.append(ls)
    header=['Name','IP','CPU',"ram",'dateandtime']
    with open('data.csv','w')as f:
        d = datetime.datetime.now()
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writeheader()
        writer.writerow({'Name':username,'IP':hostname,'CPU':lst[1].split('\n')[0],"ram":lst[2].split('\n')[0],'dateandtime':"%s-%s-%s %s:%s:%s" % (d.day, d.month, d.year,d.hour, d.minute, d.second)})


