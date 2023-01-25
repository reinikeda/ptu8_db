from sqlalchemy import Column, Integer, Float, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/banks.db')
Base = declarative_base()


class AccountNumber(Base):
    __tablename__ = 'account_number'
    id = Column(Integer, primary_key=True)
    account_number = Column(String)
    balance = Column(Float)
    owner_id = Column(Integer, ForeignKey('account_owner.id'))
    owner = relationship('AccountOwner', back_populates='account_number')
    bank_id = Column(Integer, ForeignKey('bank.id'))
    bank = relationship('Bank', back_populates='account_number')

    def __init__(self, account_number, balance, owner_id, bank_id):
        self.account_number = account_number
        self.balance = balance
        self.owner_id = owner_id
        self.bank_id = bank_id

    def __str__(self) -> str:
        return f'ID: {self.id}, account {self.account_number} was created'

class AccountOwner(Base):
    __tablename__ = 'account_owner'
    id = Column(Integer, primary_key=True)
    f_name = Column(String)
    l_name = Column(String)
    personal_code = Column(Integer)
    phone = Column(Integer)
    account_number = relationship('AccountNumber', back_populates='owner')

    def __init__(self, f_name, l_name, personal_code, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.personal_code = personal_code
        self.phone = phone

    def __str__(self) -> str:
        return f'ID: {self.id}, account owner {self.f_name} {self.l_name} was created'

class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True)
    bank_name = Column(String)
    address = Column(String)
    bank_code = Column(Integer)
    swift_code = Column(String)
    account_number = relationship('AccountNumber', back_populates='bank')

    def __init__(self, bank_name, address, bank_code, swift_code):
        self.bank_name = bank_name
        self.address = address
        self.bank_code = bank_code
        self.swift_code = swift_code

    def __str__(self) -> str:
        return f'ID: {self.id}, bank {self.bank_name} was created'

if __name__ == '__main__':
    Base.metadata.create_all(engine)