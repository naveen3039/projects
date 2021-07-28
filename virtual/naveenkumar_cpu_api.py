import datetime
import csv
import paramiko
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

username = "infinite"
hostname = "192.168.31.68"
commands = [
    "hostnamectl",
    "top -b -n1 | grep 'Cpu(s)' | awk '{print $2 + $4}' ",
    "free | grep Mem | awk '{print $4/$2 * 100.0}'"
    ]
    
    
# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#try:
client.connect(hostname=hostname, username=username)
# #except:
#     print("[!] Cannot connect to the SSH Server")
#     exit()

lst = []
for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    ls = (stdout.read().decode())
    lst.append(ls)
    error=stderr.read().decode()
    if error:
        print(error)

header=['Name','IP','CPU',"ram",'dateandtime']
with open('data.csv','w')as f:
    d = datetime.datetime.now()
    writer = csv.DictWriter(f,fieldnames=header)
    writer.writeheader()
    writer.writerow({'Name':username,'IP':hostname,'CPU':lst[1].split('\n')[0],"ram":lst[2].split('\n')[0],'dateandtime':"%s-%s-%s %s:%s:%s" % (d.day, d.month, d.year,d.hour, d.minute, d.second)})
    
emailfrom = "kumarnaveen.kumar3039@gmail.com"
emailto = "naveen.kumar5@infinite.com"
fileToSend = "data.csv"
username = "kumarnaveen.kumar3039@gmail.com"
password = ""

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
server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
#server.quit()  