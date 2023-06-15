from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class Room(Base):
    def __init__(self, room_num, type, rate):
        self._room_number = int(room_num)
        self._type = type
        self._rate = float(rate)
        self._unavailable_dates = {}

    __tablename__ = 'room'

    _room_number: Mapped[int] = mapped_column(primary_key=True)
    _type: Mapped[str]
    _rate: Mapped[float]
    #_unavailable_dates: Mapped[dict] = relationship()

    def get_room_number(self):
        return self._room_number
    
    def set_room_number(self, room_num):
        self._room_number = int(room_num)

    def get_type(self):
        return self._type

    def calculate_total(self, num_days):
        return self._rate * num_days
    
    def __repr__(self):
        return '{' + f'Room {self._room_number}: ${self._rate:.2f}' + '}'