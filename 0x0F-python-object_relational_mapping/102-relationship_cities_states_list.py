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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id)
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()
