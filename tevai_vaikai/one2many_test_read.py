from sqlalchemy.orm import sessionmaker
from one2many import Tevas, Vaikas, engine


session = sessionmaker(bind=engine)()


tevas = session.query(Tevas).filter(Tevas.vardas == "Kestutis").first()
print(tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print('-', vaikas.vardas, vaikas.pavarde)
