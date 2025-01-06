#!/usr/bin/python3
"""
List all cities and their corresponding states from the database.
This script connects to a MySQL database, queries
the `cities` and `states` tables,
and prints the city ID, city name, and associated state name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Establish a database connection using provided credentials.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    # Set up a session factory bound to the engine.
    Session = sessionmaker(bind=engine)

    # Initialize a session for performing database operations.
    session = Session()

    # Retrieve all City objects ordered by their IDs.
    for city in session.query(City).order_by(City.id):
        # Display city ID, name, and the name of the associated state.
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
