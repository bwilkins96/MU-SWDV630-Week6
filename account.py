# SWDV 630 - Object-Oriented Software Architecture
# Account class

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import Base

class Account(Base):
    def __init__(self, charge=0.0, credits=0.0):
        self._total_due = float(charge)
        self._credits = float(credits)

    __tablename__ = 'account'

    _id: Mapped[int] = mapped_column(primary_key=True)
    _total_due: Mapped[float]
    _credits: Mapped[float]

    def get_total_due(self):
        return self._total_due
    
    def get_credits(self):
        return self._credits
    
    def credit(self, amt):
        self._credits += amt

    def charge(self, amt):
        self._total_due += amt

    def pay(self, payment, credits=0):
        self._total_due -= (payment + credits)
        self._credits -= credits

    def payment_due(self):
        return self.get_total_due() > 0
    
    def __repr__(self):
        return f'<(Account) Due: ${self.get_total_due():0.2f}, Credits: ${self.get_credits():0.2f}>'