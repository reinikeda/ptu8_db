from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Project

engine = create_engine('sqlite:///data/projektai.db')
# Session = sessionmaker(bind=engine)
# session = Session()
session = sessionmaker(bind=engine)()

# CRUD - CREATE / READ / UPDATE / DELETE

# CREATE / INSERT

# naujas_projektas = Project('kazkas naujo', 14000)
# kitas_projektas = Project('kiti reikalai', 500)
# naujas_projektas = Project('brangus reikalas', 43000000)
# kitas_projektas = Project('geras puslapiukas', 50000)

# session.add(naujas_projektas)
# session.add(kitas_projektas)
# session.commit()

# READ / SELECT

# projektas1 = session.query(Project).get(1)
# projektas2 = session.query(Project).filter_by(name='geras puslapiukas').one()
# print(projektas2)

# projektai = session.query(Project).all()
# print(projektai)

# pigus_projektas = session.query(Project).filter(Project.price <= 20000).all()
# print(pigus_projektas)

# reikalai = session.query(Project).filter(Project.name.ilike('%kala%')).all()
# print(reikalai)

# UPDATE / INSERT

# brangus = session.query(Project).filter(Project.price > 1000000).first()
# brangus.price = 56000000
# session.commit()
# print(brangus)

# DELETE
# projektas1 = session.query(Project).get(2)
# session.delete(projektas1)
# session.commit()

projektai = session.query(Project).all()
print(projektai)