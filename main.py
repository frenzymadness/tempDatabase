#!/usr/bin/env python

import weather
import time
import sqlite3
import lib as l

##### TODO
# Rekalkulace prumernych hodnot aby byla spolecna pro oba druhy senzoru
# Pripojeni k databazi jeste pred ifem na rozdeleni senzoru
# V podmince mit jen to nejnutnejsi a vse ostatni spolecne ve foru
# - pripojeni k db, uzavirani db apod
# Napsat funkci pro plneni tabulek, aby se neopakoval dotaz v programu
# - preda se ji jen nazev tb, cursor a data

# Zjistime aktualni datum a cas v odpovisajicich formatech
# pro jednotlive tabulky
now = time.strftime('%Y-%m-%d %H:%M:%S')
day = time.strftime('%Y-%m-%d')
month = time.strftime('%Y-%m')
year = time.strftime('%Y')

### Pro kazdou zkoumanou lokalitu (internet, ci senzory)
### provedeme zaznam a prepocet
sensors = ['outside - internet',
          ['inside - terrarium', '81.7FD921000000'],
          ['inside - livingroom', '83.7FD921000000']]

for position in sensors:

    ### Pokud se jena o internetovou teplotu, zjistime info z netu
    # jinak zjistime ze senzoru teploty
    if position == 'outside - internet':
        # Zjistime si aktualni teplotu z internetu
        tempreature, condition = weather.weatherInfo('11782')

        # Odstranime jednotku z teploty
        tempreature = tempreature.rstrip('C')

        # Zapiseme aktualni teplotu a stav do databaze

        # Pripojeni a kurzor
        conn = sqlite3.connect('database.sqlite')
        c = conn.cursor()

        # Tuple s daty pro zapis
        data = (now, position, tempreature, condition)

        # SQL dotaz
        c.execute('INSERT INTO records VALUES (?, ?, ?, ?)', data)

        # Commit
        conn.commit()

        ### Vypocet a ulozeni prumernych hodnot
        # Pro dny
        avg_day_temp = l.get_avg_temp(c, day)
        avg_day_cond = l.get_avg_condition(c, day)
        data = (day, position, avg_day_temp, avg_day_cond)
        c.execute('INSERT OR IGNORE INTO days VALUES (?, ?, ?, ?)', data)
        conn.commit()

        # Pro mesice
        avg_month_temp = l.get_avg_temp(c, month)
        avg_month_cond = l.get_avg_condition(c, month)
        data = (month, position, avg_month_temp, avg_month_cond)
        c.execute('INSERT OR IGNORE INTO months VALUES (?, ?, ?, ?)', data)
        conn.commit()

        # Pro roky
        avg_year_temp = l.get_avg_temp(c, year)
        avg_year_cond = l.get_avg_condition(c, year)
        data = (year, position, avg_year_temp, avg_year_cond)
        c.execute('INSERT OR IGNORE INTO years VALUES (?, ?, ?, ?)', data)
        conn.commit()

        # Uzavreme spojeni s databazi
        conn.close()
    else:
        # Zde bude nasledovat totez pro senzory teploty
        name, address = position
        print 'Sensor name: %s Sensor adress: %s' % (name, address)
        pass
