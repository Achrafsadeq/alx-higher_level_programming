#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the database
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete states with 'a' in their name
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
