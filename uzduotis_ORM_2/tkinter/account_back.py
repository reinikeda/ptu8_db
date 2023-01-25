from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_db import AccountNumber, AccountOwner, Bank, engine

create_engine = create_engine('sqlite:///data/banks.db')
session = sessionmaker(bind=engine)()


def add_account(account_number, balance, owner_id, bank_id):
    account = AccountNumber(account_number, balance, owner_id, bank_id)
    session.add(account)
    session.commit()
    return account

def add_account_from_input():
    try:
        account_number = input('Account number: ')
        balance = float(input('Current balance: '))
        print('<<>> Account owners list <<>>')
        owners = session.query(AccountOwner).all()
        for owner in owners:
            print(owner.id, owner.f_name, owner.l_name)
        owner_id = int(input('Account owner id: '))
        print('<<>> Banks list <<>>')
        banks = session.query(Bank).all()
        for bank in banks:
            print(bank.id, bank.bank_name)
        bank_id = int(input('Account bank id: '))
    except ValueError:
        print('Error: Balance and ids must be a number')
    else:
        print('New account was added')
        return add_account(account_number, balance, owner_id, bank_id)


def get_all_list():
    return session.query(AccountNumber).all()