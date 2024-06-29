#!/usr/bin/python3
"""
Module 6-model_state
Defines a State class that links to the MySQL table 'states'
and creates the table in the database using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class
    Inherits from Base
    Links to the MySQL table 'states'
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

def main():
    """
    Main function that connects to the MySQL server and creates
    the 'states' table.
    """
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()

