#!/usr/bin env python

from collections import Counter


# Pro zadanou podminku vybere z db prumernou teplotu
def get_avg_temp(cursor, cond, position):
    cursor.execute('SELECT avg(tempreature) as average FROM records \
                    WHERE date like ? AND position = ?', (cond + '%',
                                                          position))
    # Zaokrouhleni hodnoty na tri desetinna mista
    return round(float(cursor.fetchone()[0]), 3)


# Pro zadanou podminku vybere z db nejcastejsi stav pocasi
def get_avg_condition(cursor, cond, position):
    cursor.execute('SELECT condition FROM records \
                    WHERE date like ? AND position = ?', (cond + '%',
                                                          position))

    # Seznam vsech stavu pocasi za dane obdobi
    data = cursor.fetchall()
    counter = Counter(data)
    return counter.most_common()[0][0][0]


# Funkce pro ukladani dat do db
def save_data(cursor, tablename, data):
    cursor.execute('INSERT OR REPLACE INTO %s VALUES (?, ?, ?, ?)'
                   % tablename, data)
