from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float

import config

user = config.DB_USER
password=config.DB_PASSWORD
db_name = config.DB_NAME
host = config.HOST

engine=create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}')