#!/usr/bin/python3
"""
Fetches all City objects from the database hbtn_0e_14_usa and displays them
in the format: <state name>: (<city id>) <city name>
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
   # Connect to the database
    db_url = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
    
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and join with State
    cities = (
        session.query(State.name, City.id, City.name)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    # Print the results
    for state_name, city_id, city_name in cities:
        print(f"{state_name}: ({city_id}) {city_name}")

    # Close the session
    session.close()
