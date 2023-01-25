from functions import *
from tkinter import *

employee_edit = False
get_all_records_list()

def update_fields():
    box.delete(0, END)
    box.insert(END, *get_all_records_list())
    entry_f_name.delete(0, 'end')
    entry_l_name.delete(0, 'end')
    entry_birth_date.delete(0, 'end')
    entry_position.delete(0, 'end')
    entry_salary.delete(0, 'end')
    entry_working_since.delete(0, 'end')

def add(event):
    global employee_edit
    if employee_edit:
        update_employee(employee_edit.id, entry_f_name.get(), entry_l_name.get(), entry_birth_date.get(), entry_position.get(), entry_salary.get(), entry_working_since.get())
        employee_edit = False
    else:
        add_employee(entry_f_name.get(), entry_l_name.get(), entry_birth_date.get(), entry_position.get(), entry_salary.get(), entry_working_since.get())
    update_fields()

def delete():
    selected = get_all_records_list()[box.curselection()[0]]
    delete_employee(selected.id)
    update_fields()

def edit():
    global employee_edit
    employee_edit = get_all_records_list()[box.curselection()[0]]
    update_fields()
    entry_f_name.insert(0, employee_edit.f_name)
    entry_l_name.insert(0, employee_edit.l_name)
    entry_birth_date.insert(0, employee_edit.birth_date)
    entry_position.insert(0, employee_edit.position)
    entry_salary.insert(0, employee_edit.salary)
    entry_working_since.insert(0, employee_edit.working_since)

window = Tk()
window.title('Employee management')
# window.iconbitmap(r'employee.ico')
window.geometry('850x345')
window.resizable(width=False, height=False)

entry_frame = Frame(window)

label_entry = Label(entry_frame, text='Enter employee')
label_f_name = Label(entry_frame, text='First name')
entry_f_name = Entry(entry_frame)
label_l_name = Label(entry_frame, text='Last name')
entry_l_name = Entry(entry_frame)
label_birth_date = Label(entry_frame, text='Date of birth')
entry_birth_date = Entry(entry_frame)
label_position = Label(entry_frame, text='Position')
entry_position = Entry(entry_frame)
label_salary = Label(entry_frame, text='Salary')
entry_salary = Entry(entry_frame)
label_working_since = Label(entry_frame, text='Working since')
entry_working_since = Entry(entry_frame)

b_enter = Button(entry_frame, text='Enter')
b_enter.bind('<Button-1>', add)
entry_f_name.bind('<Return>', add)
entry_l_name.bind('<Return>', add)
entry_birth_date.bind('<Return>', add)
entry_position.bind('Return', add)
entry_salary.bind('<Return>', add)
entry_working_since.bind('<Return>', add)
b_edit = Button(entry_frame, text='Edit', command=edit)
b_delete = Button(entry_frame, text='Delete', command=delete)

box_frame = Frame(window)

label_box = Label(box_frame, text='Employee list')
box = Listbox(box_frame, selectmode=SINGLE, width=105, height=15)
box_xscroll = Scrollbar(box_frame, orient='horizontal', command=box.xview)
box_yscroll = Scrollbar(box_frame, command=box.yview)
box.config(xscrollcommand=box_xscroll.set)
box.config(yscrollcommand=box_yscroll.set)
box.insert(END, *get_all_records_list())
b_exit = Button(box_frame, text='Exit', command=window.destroy)

entry_frame.grid(row=0, column=0, ipadx=10, ipady=10, sticky=N)
label_entry.pack()
label_f_name.pack()
entry_f_name.pack()
label_l_name.pack()
entry_l_name.pack()
label_birth_date.pack()
entry_birth_date.pack()
label_position.pack()
entry_position.pack()
label_salary.pack()
entry_salary.pack()
label_working_since.pack()
entry_working_since.pack()
b_enter.pack(side=LEFT, padx=10)
b_edit.pack(side=LEFT)
b_delete.pack(side=RIGHT, padx=10)

box_frame.grid(row=0, column=1, sticky=N)
label_box.grid(row=0, column=0, columnspan=2)
box.grid(row=1, column = 0)
box_xscroll.grid(row=2, column=0, sticky=EW)
box_yscroll.grid(row=1, column=1, sticky=NS)
b_exit.grid(row=3, column=0, columnspan=2, sticky=E, padx=10, pady=10)

window.mainloop()