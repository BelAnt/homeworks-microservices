import os
from sqlalchemy import (Column, DateTime, Integer, String, Table, create_engine, MetaData)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from databases import Database


PG_USER = os.environ.get('PG_USER', '')
PG_PASS = os.environ.get('PG_PASS', '')
PG_HOST = os.environ.get('PG_HOST', '')
PG_PORT = os.environ.get('PG_PORT', '')
DB_NAME = os.environ.get('DB_NAME', '')

DATABASE_URL = "postgresql://" + PG_USER + ":" + PG_PASS + "@" + PG_HOST + ":" + PG_PORT + "/" + DB_NAME

# SQLAlchemy
engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(256)),
    Column("firstname", String(128)),
    Column("lastname", String(128)),
    Column("email", String(128)),
    Column("phone", String(128))
)

# Databases query builder
database = Database(DATABASE_URL)
