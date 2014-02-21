#!/usr/bin/env python

import weather
import time
import sqlite3
import lib as l

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

    # Pripojeni a kurzor
    conn = sqlite3.connect('database.sqlite', isolation_level=None)
    c = conn.cursor()

    ### Pokud se jena o internetovou teplotu, zjistime info z netu
    # jinak zjistime ze senzoru teploty
    if position == 'outside - internet':
        # Zjistime si aktualni teplotu z internetu
        tempreature, condition = weather.weatherInfo('11782')

        # Odstranime jednotku z teploty
        tempreature = tempreature.rstrip('C')

    else:
        # Zde bude nasledovat totez pro senzory teploty
        name, address = position
        print 'Sensor name: %s Sensor adress: %s' % (name, address)
        continue

    # Zapis aktualnich dat
    l.save_data(c, 'records', (now, position, tempreature, condition))
    conn.commit()

    ### Vypocet a ulozeni prumernych hodnot
    # Pro dny
    avg_day_temp = l.get_avg_temp(c, day, position)
    avg_day_cond = l.get_avg_condition(c, day, position)
    l.save_data(c, 'days', (day, position, avg_day_temp, avg_day_cond))

    # Pro mesice
    avg_month_temp = l.get_avg_temp(c, month, position)
    avg_month_cond = l.get_avg_condition(c, month, position)
    l.save_data(c, 'months', (month, position,
                              avg_day_temp, avg_day_cond))

    # Pro roky
    avg_year_temp = l.get_avg_temp(c, year, position)
    avg_year_cond = l.get_avg_condition(c, year, position)
    l.save_data(c, 'years', (year, position,
                             avg_day_temp, avg_day_cond))

    # Uzavreme spojeni s databazi
    conn.commit()
    conn.close()
