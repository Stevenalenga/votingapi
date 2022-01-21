from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import false
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

SQLALCHEMY_DATA_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATA_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:

    # try:
        # conn = psycopg2.connect(host="localhost", database="myfastapi", user="postgres",
        # password="HOUSTON332", cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
        #print("database connection was successful")
        # break
    # except Exception as error:
       # print("connecting to database failed")
        #print("Error:", error)
        # time.sleep(3)
