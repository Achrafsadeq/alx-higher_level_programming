#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    username, password, database = sys.argv[1:4]
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and join with State
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Display results in the specified format
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
