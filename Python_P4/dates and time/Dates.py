import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)

print(x)

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#My example
dt = datetime.datetime(2026, 2, 22, 19, 30, 0)
print(dt)
print(dt.year)
print(dt.strftime("%A"))

d1 = datetime.datetime(2026, 2, 20)
d2 = datetime.datetime(2026, 2, 22)

difference = d2 - d1
print(difference)          
print(difference.days)     

today = datetime.datetime.now()
future = today + datetime.timedelta(days=10)
print(future)

utc_now = datetime.datetime.now(datetime.timezone.utc)
print(utc_now)