from create_db import Employee
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data/darbuotojai_alchemy_tk.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_employee(f_name, l_name, birth_date, position, salary, working_since):
    employee = Employee(f_name, l_name, birth_date, position, salary, working_since)
    session.add(employee)
    session.commit()

def update_employee(id, new_f_name, new_l_name, new_birth_date, new_position, new_salary, new_working_since):
    employee = session.query(Employee).get(id)
    employee.f_name = new_f_name
    employee.l_name = new_l_name
    employee.birth_date = new_birth_date
    employee.position = new_position
    employee.salary = new_salary
    employee.working_since = new_working_since
    session.commit()

def delete_employee(id):
    employee = session.query(Employee).get(id)
    session.delete(employee)
    session.commit()

def get_all_records_list():
    return session.query(Employee).all()