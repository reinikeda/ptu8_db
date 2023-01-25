from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/projektai.db')
Base = declarative_base()

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'({self.id}, {self.name}, {self.price}, {self.created_at})'

    def __str__(self) -> str:
        return f'ID: {self.id} - {self.name}. Kaina: {self.price}, sukurtas: {self.created_at}'

if __name__ == '__main__':
    Base.metadata.create_all(engine)