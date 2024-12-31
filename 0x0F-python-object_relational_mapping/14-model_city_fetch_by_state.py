#!/usr/bin/python3
"""
Fetches all City objects from the database hbtn_0e_14_usa and displays them
in the format: <state name>: (<city id>) <city name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Connect to the database
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and join with State
    results = (session.query(State.name, City.id, City.name)
               .join(City, State.id == City.state_id)
               .order_by(City.id)
               .all())

    # Print results
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
