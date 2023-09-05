#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    # Create an instance of the Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the necessary database tables
    Base.metadata.create_all(engine)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create an instance of the Session class
    session = Session()

    # Query and print all states and their associated cities
    records = session.query(State).order_by(State.id)
    for state in records:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

