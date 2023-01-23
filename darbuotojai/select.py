import sqlite3

conn = sqlite3.connect('data/darbuotojai.db')
c = conn.cursor()

# istraukti duomenis V1

# with conn:
#     c.execute('SELECT * FROM darbuotojai;')
#     darbuotojai = c.fetchall()

# if darbuotojai:
#     print(darbuotojai)

# istraukti duomenis V2

# with conn:
#     c.execute('SELECT * FROM darbuotojai;')
#     while True:
#         darbuotojas = c.fetchone()
#         if darbuotojas:
#             print(darbuotojas)
#         else:
#             break

#  update and delete

# with conn:
#     c.execute('UPDATE darbuotojai SET vardas="Penktadienis", pavarde="Sausiauskas" WHERE id=6;')
#     c.execute('DELETE FROM darbuotojai WHERE id=7;')

#     c.execute('SELECT * FROM darbuotojai;')
#     while True:
#         darbuotojas = c.fetchone()
#         if darbuotojas:
#             print(darbuotojas)
#         else:
#             break

