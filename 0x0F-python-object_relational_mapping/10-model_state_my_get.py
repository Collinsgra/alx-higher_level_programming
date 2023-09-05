#!/usr/bin/python3
"""Prints states objs"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from sqlalchemy import exc

    # Creates db instance
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    try:
        record = session.query(State).filter(State.name == sys.argv[4]).one()
        print("{}".format(record.id))
    except exc.SQLAlchemyError:
        print("Not found")
