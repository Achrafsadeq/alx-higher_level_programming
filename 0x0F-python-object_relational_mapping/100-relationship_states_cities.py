#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    username, password, database = sys.argv[1:4]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}", pool_pre_ping=True)

    # Create all tables in the database
    from relationship_state import Base
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" with the City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    # Add to session and commit
    session.add(new_state)
    session.commit()

    session.close()
