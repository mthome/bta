#!/usr/bin/env python

import myfitnesspal
import sys
from datetime import timedelta, datetime, date

nd = 30
oneday = timedelta(days=1)

d2 = date.today()
d1 = d2 - nd * oneday

username = sys.argv[1]
client = myfitnesspal.Client(username)
weights = client.get_measurements('Weight', d1, d2)
steps = client.get_measurements('Fitbit steps', d1, d2)
weight = 0

for i in range(0,nd):
    d = d1+i*oneday
    carbs = 0
    cals = 0
    try:
        weight = weights[d]
    except:
        pass

    try:
        step = int(steps[d])
    except:
        step = 0

    try:
        data = client.get_date(d1+i*oneday)
        meals = data.meals
        # notes = data.notes
        totals = data.totals
        carbs = totals['carbohydrates']
        cals = totals['calories']
    except:
        pass
    print("{date} {weight} {steps} {carbs} {cals}".
          format(date=d,
                 weight=weight,
                 steps=step,
                 carbs=carbs,
                 cals=cals))


