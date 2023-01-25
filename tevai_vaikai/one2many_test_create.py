from sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine

session = sessionmaker(bind=engine)()


daiva = Tevas(vardas='Daiva', pavarde='Reinike')
otas = Vaikas(vardas='Otas', pavarde='Reinikis')
lakis = Vaikas(vardas='Lakis', pavarde='Katinauskas')

# 1 variantas:
daiva.vaikai.append(otas)
daiva.vaikai.append(lakis)
session.add(daiva)

# 2 variantas:
# daiva.vaikai = (otas, lakis)

# 3 variantas:
# otas.tevas = daiva
# lakis.tevas = daiva
# session.add(otas)
# session.add(lakis)

session.commit()