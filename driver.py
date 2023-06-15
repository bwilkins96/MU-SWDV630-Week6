from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from base import Base
from room import Room
from person import Guest, Employee, Manager

def main():
    # Creates a database in the directory called 'test.db'
    #engine = create_engine("sqlite+pysqlite:///test.db", echo=False)
    
    # Creates a transient in-memory database
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)
    
    Base.metadata.create_all(engine)

    room = Room(152, 'queen', 100)
    guest = Guest(room, 'Joe')
    employee = Employee(20, 'Jeff')
    
    manager = Manager('B10', 30, 'Jenny')
    manager.add_employee(employee)

    data = [room, guest, employee, manager]
    classes = [Room, Guest, Employee, Manager]

    print()
    with Session(engine) as session:
        for obj in data:
            session.add(obj)
        session.commit()

        for cls in classes:
            print(cls)
            stmt = select(cls)
            result = session.scalars(stmt)
            
            for inst in result.all():
                print(inst)
            print()

if __name__ == '__main__': main()