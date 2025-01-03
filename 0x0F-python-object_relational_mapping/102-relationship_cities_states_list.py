#!/usr/bin/python3
"""
List all cities and their corresponding states from the database.
This script connects to a MySQL database, queries the `cities` and `states` tables,
and prints the city ID, city name, and associated state name.
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        sys.exit(1)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).\
                        join(State, State.id == City.state_id).\
                        order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
