from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated

sqlite_file_name = "my_database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tabels():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

