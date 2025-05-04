from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib.parse

encoded_password=urllib.parse.quote_plus("Q1w2e3r4@@")
DATABASE_URL = "mysql+aiomysql://root:{0}@localhost/archery_club".format(encoded_password)
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine,
    class_=AsyncSession)

Base = declarative_base()