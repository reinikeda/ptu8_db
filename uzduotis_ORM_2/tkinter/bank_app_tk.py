from tkinter import *
from bank_back import *
from account_back import *
from owner_back import *

# get_all_list()

def check_banks():
    bank_window = Toplevel(bank_window)

def check_owners():
    pass

def check_accounts():
    pass
    # window_account = Toplevel()

window = Tk()
window.title('BOA: Banks, Owners, Accounts')
window.geometry('750x300')
window.configure(bg='#fef9e7')

main_window = Frame(window, bg='#fef9e7')
b_new_bank = Button(main_window, text='Add new bank', width=15, bg='#fad7a0')
b_new_owner = Button(main_window, text='Add new account owner', width=15, bg='#fad7a0')
b_new_account = Button(main_window, text='Add new account number', width=15, bg='#fad7a0')
b_check_banks = Button(main_window, text='Check banks information', width=15, bg='#fad7a0', command=check_banks)
b_check_owners = Button(main_window, text='Check account owners information', width=15, bg='#fad7a0', command=check_owners)
b_check_accounts = Button(main_window, text='Check accounts information', width=15, bg='#fad7a0', command=check_accounts)
b_exit = Button(main_window, text='Exit', width=15, bg='#fad7a0', command=window.destroy)

main_window.pack()
b_new_bank.grid(row=0, column=0, ipady=10, ipadx=40, pady=20, padx=20)
b_new_owner.grid(row=0, column=1, ipady=10, ipadx=40, pady=20, padx=20)
b_new_account.grid(row=0, column=2, ipady=10, ipadx=40, pady=20, padx=20)
b_check_banks.grid(row=1, column=0, ipady=10, ipadx=40, padx=20)
b_check_owners.grid(row=1, column=1, ipady=10, ipadx=40, padx=20)
b_check_accounts.grid(row=1, column=2, ipady=10, ipadx=40, padx=20)
b_exit.grid(row=2, column=2, ipady=10, ipadx=40, pady=40, padx=20)

window.mainloop()