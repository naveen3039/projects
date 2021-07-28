from dotenv import load_dotenv
import os

load_dotenv()
DATABASE = os.environ["DATABASE"]
USER = os.environ["NAME"]
PASSWORD = os.environ["PASSWORD"]
HOST = os.environ["HOST"]
