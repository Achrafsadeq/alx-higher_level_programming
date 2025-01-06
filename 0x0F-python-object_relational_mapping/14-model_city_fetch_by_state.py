#!/usr/bin/python3
"""Script to list all City objects from database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name)\
        .join(City, State.id == City.state_id)\
        .order_by(City.id)

    for state_name, city_id, city_name in cities:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
