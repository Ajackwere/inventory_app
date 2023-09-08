# This will initialize the db connection, create tables, and manage my sessions. Alembic will also be configured here
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from alembic.config import Config
DB_URL = 'sqlite:///inventory.db'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)


def create_migration():
    alembic_cfg = Config("alembic.ini")
    command_revision(alembic_cfg, autogenerate=True)
