import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, DateTime, DATETIME
from database import Base
from database import ENGINE
from datetime import datetime

class Co2Concentrate(Base):
    __tablename__ = 'co2_concentrates'
    id = Column('id', Integer, primary_key=True)
    concentrate = Column('concentrate', Float)
    created = Column('created', DATETIME, default=datetime.now, nullable=False)


def main(args):
    # Base.metadata.drop_all(bind=ENGINE)
    Base.metadata.create_all(bind=ENGINE)


if __name__ == '__main__':
    main(sys.argv)
