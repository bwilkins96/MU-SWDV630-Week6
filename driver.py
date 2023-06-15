from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from base import Base
from room import Room

def main():
    #engine = create_engine("sqlite+pysqlite:///test.db", echo=False)
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    rooms = []
    for i in range(1, 6):
        rooms.append(Room(i, 'queen', 150))

    with Session(engine) as session:
        for room in rooms:
            session.add(room)
        session.commit()

        stmt = select(Room)
        result = session.scalars(stmt)
        
        for room in result.all():
            print(room)


if __name__ == '__main__': main()