#!/usr/bin env python

from collections import Counter


# Pro zadanou podminku vybere z db prumernou teplotu
def get_avg_temp(cursor, cond):
    cursor.execute('SELECT avg(tempreature) as average FROM records \
                    WHERE date like ?', (cond + ' %', ))
    return cursor.fetchone()[0]


# Pro zadanou podminku vybere z db nejcastejsi stav pocasi
def get_avg_condition(cursor, cond):
    cursor.execute('SELECT condition FROM records \
                    WHERE date like ?', (cond + ' %', ))

    # Seznam vsech stavu pocasi za dane obdobi
    data = cursor.fetchall()
    counter = Counter(data)
    return counter.most_common()[0][0]
