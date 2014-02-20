#!/usr/bin/env python

import weather
import time
import sqlite3

# Zjistime aktualni datum a cas v odpovisajicich formatech
# pro jednotlive tabulky
now = time.strftime('%Y-%m-%d %H:%M:%S')
day = time.strftime('%Y-%m-%d')
month = time.strftime('%Y-%m')
year = time.strftime('%Y')

# Pro kazdou zkoumanou lokalitu (internet, ci senzory)
# provedeme zaznam a prepocet
sensors = ['outside - internet',
          ['inside - terrarium', '81.7FD921000000'],
          ['inside - livingroom', '83.7FD921000000']]

for position in sensors:

    # Pokud se jena o internetovou teplotu, zjistime info z netu
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

        # Uzavreme spojeni s databazi
        conn.close()
    else:
        # Zde bude nasledovat totez pro senzory teploty
        name, address = position
        print 'Sensor name: %s Sensor adress: %s' % (name, address)
        pass
