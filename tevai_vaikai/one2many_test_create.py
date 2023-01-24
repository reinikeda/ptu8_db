from sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine


session = sessionmaker(bind=engine)()


kestutis = Tevas(vardas="Kestutis", pavarde="Januskevicius")
emilija = Vaikas(vardas="Emilija", pavarde="Januskeviciute")
maja = Vaikas(vardas="Maja", pavarde="Januskeviciute")
marco = Vaikas(vardas="Marco", pavarde="Januskevicius")

# pirmas
kestutis.vaikai.append(emilija)
kestutis.vaikai.append(maja)
kestutis.vaikai.append(marco)
session.add(kestutis)

# # alternatyviai, jeigu dar nera kitu vaiku
# kestutis.vaikai = [emilija, maja, marco]
# session.add(kestutis)

# # antras
# emilija.tevas = kestutis
# maja.tevas = kestutis
# marco.tevas = kestutis
# session.add(emilija)
# session.add(maja)
# session.add(marco)

session.commit()


