#!/usr/bin/python3
"""Lists all States"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    # Creates db instance
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
