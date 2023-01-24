from sqlalchemy.orm import sessionmaker
from many2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

print('--- tevai su vaikais ---')
tevas = session.query(Tevas).filter_by(vardas="Kestutis").one()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

mama = session.query(Tevas).filter_by(vardas="Nicoletta").one()
print(mama.vardas, mama.pavarde)
for vaikas in mama.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

print('--- vaikai su tevais ---')
vaikai = session.query(Vaikas).all()
for vaikas in vaikai:
    print(vaikas.vardas, vaikas.pavarde)
    for vaiko_tevas in vaikas.tevai:
        print('-', vaiko_tevas.vardas, vaiko_tevas.pavarde)
