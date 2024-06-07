from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://yugwmtqdyb_aptex:-CA!2.0GYc-f8F%m@s46.cyber-folks.pl:3306/yugwmtqdyb_aptex'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()