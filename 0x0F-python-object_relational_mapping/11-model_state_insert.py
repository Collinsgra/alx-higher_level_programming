#!/usr/bin/python3
"""Adds states"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    # Creates db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    Louisiana = State(name='Louisiana')
    session.add(Louisiana)
    session.commit()
    print("{}".format(Louisiana.id))
