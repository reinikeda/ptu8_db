# Parašykite programą, kuri leistų vartotojui per konsolę:
# įvesti naują eilutę (automobilį su visais parametrais)
# ieškoti įrašų pagal visus stulpelius. Vartotojas gali pasirinkti kuriuos parametrus paieškoje praleisti. Metus ir kainą vartotojas turėtų nurodinėti nuo -iki.

import sqlite3

conn = sqlite3.connect('data/uzduotis_auto.db')
c = conn.cursor()

while True:
    print('<---> AUTOMOBILIŲ DUOMENŲ BAZĖ <--->')
    print('Naujas įrašas - 1')
    print('Paieška - 2')
    print('Išeiti - enter')
    uzklausa = input('Pasirinkite ką norite daryti: ')
    if uzklausa == '':
        break
    if uzklausa == '1':
        print('<---> NAUJAS IRAŠAS <--->')
        auto_marke = input('Įveskite automobilio gamintojo markę: ')
        auto_modelis = input('Įveskite automobilio modelį: ')
        auto_spalva = input('Įveskite automobilio spalvą: ')
        auto_metai = int(input('Įveskite automobilio pagaminimo metus: '))
        auto_kaina = float(input('Įveskite automobilio kainą: '))
        with conn:
            c.execute('INSERT INTO automobiliai (automobilio_marke, modelis, spalva, pagaminimo_metai, kaina) VALUES (?, ?, ?, ?, ?)', (auto_marke, auto_modelis, auto_spalva, auto_metai, auto_kaina))
    if uzklausa == '2':
        print('<---> PAIEŠKA <--->')
        paieskos_tipas = input('Ar norite ieškoti tarp visų duomenų? T/N: ')
        if paieskos_tipas.lower() == "t":
            paieska = input('Paieška: ')
            paieska = f'%{paieska}%'
            with conn:
                c.execute('SELECT * FROM automobiliai WHERE automobilio_marke LIKE ? OR modelis LIKE ? OR spalva LIKE ? OR pagaminimo_metai LIKE ? OR kaina LIKE ?', (paieska, paieska, paieska, paieska, paieska))
                while True:
                    auto = c.fetchone()
                    if auto:
                        print(auto)
                    else:
                        print('Gauti visi rezultatai atitinkantys paieškos parametrus')
                        break
        if paieskos_tipas.lower() == 'n':
            print('Nurodykite atskirus paieškos parametrus')
            auto_marke = input('Ieškoti tarp automobilių markių: ')
            auto_marke = f'%{auto_marke}%'
            auto_modelis = input('Ieškoti tarp automobilių modelių: ')
            auto_modelis = f'%{auto_modelis}%'
            auto_spalva = input('Ieškoti tarp automobilių spalvų: ')
            auto_spalva = f'%{auto_spalva}%'
            auto_metai_nuo = input('Ieškoti automobilių metų nuo: ')
            auto_metai_iki = input('Ieškoti automobilių metų iki: ')
            auto_kaina_nuo = input('Ieškoti automobilių kainos nuo: ')
            auto_kaina_iki = input('Ieškoti automobilių kainos iki: ')
            with conn:
                pasirinkimas = 'SELECT * FROM automobiliai WHERE automobilio_marke LIKE ? AND modelis LIKE ? AND spalva LIKE ?'
                argumentai = [auto_marke, auto_modelis, auto_spalva]
                if auto_metai_nuo:
                    pasirinkimas += ' AND pagaminimo_metai >= ?'
                    auto_metai_nuo = int(auto_metai_nuo)
                    argumentai.append(auto_metai_nuo)
                if auto_metai_iki:
                    pasirinkimas += ' AND pagaminimo_metai <= ?'
                    auto_metai_iki = int(auto_metai_iki)
                    argumentai.append(auto_metai_iki)
                if auto_kaina_nuo:
                    pasirinkimas += ' AND kaina >= ?'
                    auto_kaina_nuo = float(auto_kaina_nuo)
                    argumentai.append(auto_kaina_nuo)
                if auto_kaina_iki:
                    pasirinkimas += ' AND kaina <= ?'
                    auto_kaina_iki = float(auto_kaina_iki)
                    argumentai.append(auto_kaina_iki)
                c.execute(pasirinkimas, argumentai)
                while True:
                    auto = c.fetchone()
                    if auto:
                        print(auto)
                    else:
                        print('Gauti visi rezultatai atitinkantys paieškos parametrus')
                        break