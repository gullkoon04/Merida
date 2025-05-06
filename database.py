# database.py
import os
import urllib.parse
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1) 환경변수에서 꺼내기 (docker-compose.yml 에 설정해 둔 값들)
USER     = os.getenv("MYSQL_USER",     "root")
PASSWORD = os.getenv("MYSQL_PASSWORD", "Q1w2e3r4@@")          # 기본값은 로컬 테스트용
HOST     = os.getenv("DB_HOST",       "db")                   # Compose 네트워크의 서비스명
PORT     = os.getenv("DB_PORT",       "3306")
NAME     = os.getenv("MYSQL_DATABASE","archery_club")

# 2) 비밀번호에 특수문자 있을 경우 인코딩
pwd = urllib.parse.quote_plus(PASSWORD)

DATABASE_URL = (
    f"mysql+aiomysql://{USER}:{pwd}@{HOST}:{PORT}/{NAME}"
)

# 3) Async SQLAlchemy 엔진 & 세션
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
)

Base = declarative_base()
