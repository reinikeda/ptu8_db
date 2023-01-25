from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_db import AccountOwner, engine

create_engine = create_engine('sqlite:///data/banks.db')
session = sessionmaker(bind=engine)()


def add_owner(f_name, l_name, personal_code, phone):
    owner = AccountOwner(f_name, l_name, personal_code, phone)
    session.add(owner)
    session.commit()
    return owner

def add_owner_from_input():
    try:
        f_name = input('First name: ')
        l_name = input('Last name: ')
        personal_code = int(input('Personal code: '))
        phone = int(input('Phone number: '))
    except ValueError:
        print('Error: Personal code and phone number must be a number')
    else:
        print('New account owner was added')
        return add_owner(f_name, l_name, personal_code, phone)

def get_all_list():
    return session.query(AccountOwner).all()