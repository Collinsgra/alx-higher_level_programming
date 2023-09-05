#!/usr/bin/python3
"""Changes name of state"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from sqlalchemy import exc

    # Creates db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    try:
        record = session.query(State).filter(State.id == '2').one()
        record.name = 'New Mexico'
        session.commit()
    except exc.SQLAlchemyError:
        print("State id not found")
