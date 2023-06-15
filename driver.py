from sqlalchemy import create_engine, select

from sqlalchemy import String, Integer, ForeignKey, Column
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    pass

class Test(Base):
    def __init__(self, name):
        self.name = name

    __tablename__ = 'test_table'

    id = mapped_column(Integer(), primary_key=True)
    name = mapped_column(String(50))

def main():
    #engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

    engine = create_engine("sqlite+pysqlite:///test.db", echo=False)
    Base.metadata.create_all(engine)

    test = Test('This is not final, this is just a test!')

    with Session(engine) as session:
        session.add(test)
        session.commit()

        stmt = select(Test).where(Test.name == 'This is not final, this is just a test!')
        result = session.scalars(stmt)
        
        for t in result.all():
            print(t)


if __name__ == '__main__': main()