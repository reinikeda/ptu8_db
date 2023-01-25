from create_db import Employee, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

session = sessionmaker(bind=engine)()

def employee_menu():
    print('<<<>>> EMPLOYEE MANAGEMENT <<<>>>')
    print('1 | Add new employee')
    print('2 | View current employees')
    print('3 | Update employee information')
    print('4 | Delete employee')
    print('0 | Exit')
    choice = input('Make a choice: ')
    return choice

def add_employee(f_name, l_name, birth_date, position, salary):
    employee = Employee(f_name, l_name, birth_date, position, salary)
    session.add(employee)
    session.commit()
    print(employee)
    return employee

def add_employee_from_input():
    try:
        f_name = input('First name: ')
        l_name = input('Last name: ')
        birth_date = datetime.strptime(input('Date of birth: '), ('%Y-%m-%d')).date()
        position = input('Position: ')
        salary = float(input('Salary: '))
    except ValueError:
        print('Error! Date format is YYYY-MM-DD and salary must be a number')
    else:
        return add_employee(f_name, l_name, birth_date, position, salary)

def employee_list(query=session.query(Employee)):
    if len(query.all()) > 0:
        for employee in query.all():
            print(employee)
    else:
        print('--- No employees found ---')

def get_by_id():
    employee_list()
    try:
        id = int(input('Enter employee ID: '))
    except ValueError:
        print('ID must be a number')
    else:
        return session.query(Employee).get(id)

def update_employee(employee, **kwargs):
    for column, value in kwargs.items():
        if value:
            setattr(employee, column, value)
    session.commit()
    print(employee)

def collect_changes(employee):
    print(employee)
    print('Enter new parameters or nothing to leave')
    changes = {
        'f_name': input('First name:'),
        'l_name': input('Last Name: '),
        'birth_date': input('Date of birth: '),
        'position': input('Position: '),
        'salary': input('Salary: '),
    }
    return changes

def delete_employee(employee):
    print(f'Deleting employee with ID: {employee.id}')
    session.delete(employee)
    session.commit()

while True:
    choice = employee_menu()
    if choice == '0' or choice == '':
        break
    elif choice == '1':
        add_employee_from_input()
    elif choice == '2':
        employee_list()
    elif choice == '3':
        employee = get_by_id()
        update_employee(employee, **collect_changes(employee))
    elif choice == '4':
        delete_employee(get_by_id())
    else:
        print(f'Error! Wrong choice: {choice}')