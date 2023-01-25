from sqlalchemy.orm import sessionmaker
from create_db import AccountNumber, AccountOwner, Bank, engine
import os

session = sessionmaker(bind=engine)()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_menu():
    print('<<<>>> MENU <<<>>>')
    print('1 | Add new bank')
    print('2 | Add new account owner')
    print('3 | Add new account number')
    print('4 | Check account information')
    print('5 | Check all information')
    print('0 | Exit')
    choice = input('Make a choice: ')
    return choice

def add_bank(bank_name, address, bank_code, swift_code):
    bank = Bank(bank_name, address, bank_code, swift_code)
    session.add(bank)
    session.commit()
    return bank

def add_bank_from_input():
    try:
        bank_name = input('Bank name: ')
        address = input('Bank address: ')
        bank_code = int(input('Bank code: '))
        swift_code = input('Swift code: ')
    except ValueError:
        print('Error: Bank code must be a number')
    else:
        print('New bank was added')
        return_menu = input('Press any key to return to menu: ')
        if return_menu:
            return
        return add_bank(bank_name, address, bank_code, swift_code)

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
        return_menu = input('Press any key to return to menu: ')
        if return_menu:
            return
        return add_owner(f_name, l_name, personal_code, phone)

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
        return_menu = input('Press any key to return to menu: ')
        if return_menu:
            return
        return add_account(account_number, balance, owner_id, bank_id)

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
                return_menu = input('Press any key to return to menu: ')
                if return_menu:
                    return

def check_all():
    print('<<>> Banks list <<>>')
    banks = session.query(Bank).all()
    for bank in banks:
        print(bank.id, bank.bank_name)
    print('<<>> Account owners list <<>>')
    owners = session.query(AccountOwner).all()
    for owner in owners:
        print(owner.id, owner.f_name, owner.l_name)
    print('<<>> Account list <<>>')
    account = session.query(AccountNumber).all()
    for account in account:
        print(account.id, account.account_number, account.balance, '€')
    return_menu = input('Press any key to return to menu: ')
    if return_menu:
        return
    

while True:
    clear()
    choice = print_menu()
    if choice == '0' or choice == '':
        break
    elif choice == '1':
        add_bank_from_input()
    elif choice == '2':
        add_owner_from_input()
    elif choice == '3':
        add_account_from_input()
    elif choice == '4':
        check_account()
    elif choice == '5':
        check_all()
    else:
        print(f'Error: choice {choice} doesn\'t exist')