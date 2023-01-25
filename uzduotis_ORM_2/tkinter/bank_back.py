from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_db import Bank
from tkinter import *

engine = create_engine('sqlite:///data/banks.db')
session = sessionmaker(bind=engine)()

def add_bank(bank_name, address, bank_code, swift_code):
    bank = Bank(bank_name, address, bank_code, swift_code)
    session.add(bank)
    session.commit()

def add_bank_from_input():
    bank_name = input('Bank name: ')
    address = input('Bank address: ')
    bank_code = int(input('Bank code: '))
    swift_code = input('Swift code: ')
    return add_bank(bank_name, address, bank_code, swift_code)

def get_all_list():
    return session.query(Bank).all()

bank_window = Tk()
bank_window.title('BOA: Banks, Owners, Accounts')
bank_window.geometry('750x300')
bank_window.configure(bg='#fef9e7')

bank_window.mainloop()