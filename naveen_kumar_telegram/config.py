from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get("token")
chat_id = os.environ.get("chat_id")
username = os.environ.get("username")
hostname = os.environ.get("hostname")
server_password = os.environ.get("server_password")
emailfrom = os.environ.get("emailfrom")
emailto = os.environ.get("emailto")
email_password = os.environ.get("email_password")
