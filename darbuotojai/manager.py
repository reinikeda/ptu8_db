import sqlite3

conn = sqlite3.connect('data/darbuotojai.db')
c = conn.cursor()

while True:
    print('Neveskite nieko, kad iseiti')
    paieska = input('Ko ieskom? ')
    if paieska == '':
        break
    else:
        paieska = f'%{paieska}%'
        with conn:
            # c.execute(f'SELECT * FROM darbuotojai WHERE pavarde LIKE "%{paieska}%" OR vardas LIKE "%{paieska}%"')
            # f stringa galima nulauzti input irase pvz || "OR 1=1 --
            # saugesnis variantas:
            c.execute('SELECT * FROM darbuotojai WHERE pavarde LIKE ? OR vardas LIKE ?', (paieska, paieska))
            while True:
                darbuotojas = c.fetchone()
                if darbuotojas:
                    print(darbuotojas)
                else:
                    print('...daugiau nera')
                    break