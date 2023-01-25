from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_db import AccountNumber, AccountOwner, engine

create_engine = create_engine('sqlite:///data/banks.db')
session = sessionmaker(bind=engine)()


def check_account():
    print('<<>> Account owners list <<>>')
    owners = session.query(AccountOwner).all()
    for owner in owners:
        print(owner.id, owner.f_name, owner.l_name)
    try:
        check_owner = int(input('Account owner id: '))
    except ValueError:
        print('ID must be a number')
    else:
        print(f'<<>> All accounts of chosen owner <<>>')
        accounts = session.query(AccountNumber).filter_by(owner_id=check_owner).all()
        for account in accounts:
            print(account.id, account.account_number, account.balance, '€')
        try:
            check_account = int(input('Select account ID to make changes to balance (or enter to return): '))
        except ValueError:
            print('ID must be a number')
        else:
            if check_account == '':
                return
            else:
                change_balance = float(input('New balance: '))
                current_account = session.query(AccountNumber).get(check_account)
                current_account.balance = change_balance
                session.commit()
                print('Balance was updated')
                return

def get_all_list():
    return session.query(AccountNumber).all()