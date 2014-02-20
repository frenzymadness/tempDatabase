#!/usr/bin/env python

import weather
import time
import sqlite3

# Zjistime si aktualni teplotu z internetu
tempreature, condition = weather.weatherInfo('11782')

# Odstranime jednotku z teploty
tempreature = tempreature.rstrip('C')

# Zjistime aktualni datum a cas v odpovisajicich formatech
# pro jednotlive tabulky
now = time.strftime('%Y-%m-%d %H:%M:%S')
day = time.strftime('%Y-%m-%d')
month = time.strftime('%Y-%m')
year = time.strftime('%Y')

# Zapiseme aktualni teplotu a stav do databaze

# Pripojeni a kurzor
conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

# Tuple s daty pro zapis
data = (now, 'outside - internet', tempreature, condition)

# SQL dotaz
c.execute('INSERT INTO records VALUES (?, ?, ?, ?)', data)

# Commit
conn.commit()

# Uzavreme spojeni s databazi
conn.close()
