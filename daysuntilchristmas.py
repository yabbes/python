from datetime import date

today = date.today()
christmas = date(2017,12,25)
delta = christmas - today

print(delta.days)
