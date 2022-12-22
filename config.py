import os
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("USER_NAME")
DB_PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
