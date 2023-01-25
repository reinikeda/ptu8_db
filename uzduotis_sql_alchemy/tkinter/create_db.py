from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/darbuotojai_alchemy_tk.db')
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    f_name = Column(String)
    l_name = Column(String)
    birth_date = Column(String)
    position = Column(String)
    salary = Column(Float)
    working_since = Column(String)

    def __init__(self, f_name, l_name, birth_date, position, salary, working_since):
        self.f_name = f_name
        self.l_name = l_name
        self.birth_date = birth_date
        self.position = position
        self.salary = salary
        self.working_since = working_since

    def __repr__(self) -> str:
        return f'({self.id}, {self.f_name}, {self.l_name}, {self.birth_date}, {self.position}, {self.salary}, {self.working_since})'

    def __str__(self) -> str:
        return f'ID: {self.id}, employee: {self.f_name} {self.l_name}, birth date: {self.birth_date}, position: {self.position}, salary: {self.salary} €, working since: {self.working_since}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)