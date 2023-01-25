from sqlalchemy.orm import sessionmaker
from many2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

print('--- tevai su vaikais ---')
tevas = session.query(Tevas).filter_by(vardas='Daiva').one()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

zymantas = session.query(Tevas).filter_by(vardas='Zymantas').one()
print(zymantas.vardas, zymantas.pavarde)
for vaikas in zymantas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

print('--- vaikas su tevais ---')
vaikai = session.query(Vaikas).all()
for vaikas in vaikai:
    print(vaikas.vardas, vaikas.pavarde)
    for vaiko_tevas in vaikas.tevai:
        print('-', vaiko_tevas.vardas, vaiko_tevas.pavarde)

# print('--- vaikas su tevais ---')
# otas = session.query(Vaikas).filter_by(vardas='Otas').one()
# print(otas.vardas, otas.pavarde)
# for oto_mama in otas.tevai:
#     print('-', oto_mama.vardas, oto_mama.pavarde)

# lakis = session.query(Vaikas).filter_by(vardas='Lakis').one()
# print(lakis.vardas, lakis.pavarde)
# for lakio_mama in lakis.tevai:
#     print('-', lakio_mama.vardas, lakio_mama.pavarde)