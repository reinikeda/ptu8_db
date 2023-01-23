import sqlite3
import os
# from random import randint

if not os.path.exists('data'):
    os.mkdir('data')

conn = sqlite3.connect('data/uzduotis_auto.db')

with conn:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS automobiliai (
            id INTEGER PRIMARY KEY NOT NULL,
            automobilio_marke VARCHAR(50) NOT NULL,
            modelis VARCHAR(50) NOT NULL,
            spalva VARCHAR(20) NOT NULL,
            pagaminimo_metai INTEGER(4) NOT NULL,
            kaina DECIMAL(10,2)
        )
    """)

    automobiliai = [
        ('Chevrolet', 'Express', 'Goldenrod', 2011, 15887.22),
        ('Cadillac', 'XLR-V', 'Goldenrod', 2007, 23732.96),
        ('Mitsubishi', '3000GT', 'Violet', 1992, 49161.36),
        ('Mazda', '626', 'Mauv', 1996, 26184.84),
        ('Toyota', 'Sienna', 'Puce', 2001, 34037.33),
        ('Buick', 'Rainier', 'Blue', 2005, 29424.17),
        ('Buick', 'LeSabre', 'Crimson', 1987, 13439.71),
        ('Dodge', 'Intrepid', 'Purple', 1997, 15595.77),
        ('Honda', 'Pilot', 'Mauv', 2008, 5244.06),
        ('Audi', 'A6', 'Goldenrod', 2001, 1969.93),
        ('Lexus', 'LS', 'Maroon', 1989, 46396.64),
        ('Kia', 'Sportage', 'Pink', 2006, 15668.53)
    ]
    c.executemany('INSERT INTO automobiliai (automobilio_marke, modelis, spalva, pagaminimo_metai, kaina) VALUES (?, ?, ?, ?, ?)', automobiliai)


    # for kaina in randint(1000, 50000):
    #     automobiliai = [
    #         ('Chevrolet', 'Express', 'Goldenrod', 2011, kaina),
    #         ('Cadillac', 'XLR-V', 'Goldenrod', 2007, kaina),
    #         ('Mitsubishi', '3000GT', 'Violet', 1992, kaina),
    #         ('Mazda', '626', 'Mauv', 1996, kaina),
    #         ('Toyota', 'Sienna', 'Puce', 2001, kaina),
    #         ('Buick', 'Rainier', 'Blue', 2005, kaina),
    #         ('Buick', 'LeSabre', 'Crimson', 1987, kaina),
    #         ('Dodge', 'Intrepid', 'Purple', 1997, kaina),
    #         ('Honda', 'Pilot', 'Mauv', 2008, kaina),
    #         ('Audi', 'A6', 'Goldenrod', 2001, kaina),
    #         ('Lexus', 'LS', 'Maroon', 1989, kaina),
    #         ('Kia', 'Sportage', 'Pink', 2006, kaina)
    #     ]
    #     c.executemany('INSERT INTO automobiliai (automobilio_marke, modelis, spalva, pagaminimo_metai, kaina) VALUES (?, ?, ?, ?, ?)', automobiliai)