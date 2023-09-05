#!/usr/bin/python3
"""Lists all the cities"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import relationship

    # Creates db database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    record = session.query(City).order_by(City.id)
    for city in record:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
