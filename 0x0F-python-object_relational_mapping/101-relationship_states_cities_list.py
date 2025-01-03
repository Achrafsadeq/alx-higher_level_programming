#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in
the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Capture the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection_string = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database
    )

    engine = create_engine(connection_string)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
