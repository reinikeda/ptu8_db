from sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

print('--- tevas su vaikais ---')
tevas = session.query(Tevas).filter(Tevas.vardas == 'Daiva').first()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)

print('--- tevo vaikas ---')
lakis = session.query(Vaikas).filter(Vaikas.vardas == 'Lakis').first()
print(lakis.vardas, 'tevas yra', lakis.tevas.vardas)

print('--- vaiko tevo pirmas vaikas ---')
pliurpaburnis = lakis.tevas.vaikai[0]
print(pliurpaburnis.vardas)

print('--- vaikas pakoreguota pavarde ---')
pliurpaburnis.pavarde = 'Pliurpaburniauskas'
session.commit()
print(pliurpaburnis.vardas, pliurpaburnis.pavarde)

# panaikina rysi, bet neistrina vaiko
lakis = tevas.vaikai[1]
if lakis.vardas == 'Lakis':
    tevas.vaikai.remove(lakis)
else:
    print('Lakis jau yra ', lakis.vardas)
session.commit()