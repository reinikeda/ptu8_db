from sqlalchemy.orm import sessionmaker
from many2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()

# daiva = Tevas(vardas='Daiva', pavarde='Reinike')
# otas = Vaikas(vardas='Otas', pavarde='Reinikis')
# daiva.vaikai.append(otas)
# session.add(daiva)
# session.commit()

# zymantas = Tevas(vardas='Zymantas', pavarde='Reinikis')
# otas = session.query(Vaikas).filter_by(vardas='Otas').one()
# if otas:
#     zymantas.vaikai.append(otas)
# session.add(zymantas)
# session.commit()

tevai = session.query(Tevas).filter(Tevas.pavarde.ilike('Rein%')).all()
# tevai[0].pavarde = 'Nauja pavarde' <- regadavimas
lakis = Vaikas(vardas='Lakis', pavarde='Katinauskas', tevai=tevai)
session.add(lakis)
session.commit()