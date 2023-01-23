import sqlite3

conn = sqlite3.connect('data/darbuotojai.db')
c = conn.cursor()

while True:
    print('Atskyrimas kambeliais, nieko, kad iseiti')
    paieska = input('Iveskite ID: ')
    if paieska == '':
        break
    else:
        ids = paieska.split(',')
        with conn:
            query = "SELECT * FROM darbuotojai WHERE rowid IN (" + ', '.join(['?' for x in range(len(ids))]) + ")"
            print(query)
            c.execute(query, ids)
            while True:
                darbuotojas = c.fetchone()
                if darbuotojas:
                    print(darbuotojas)
                else:
                    print('...daugiau nera')
                    break