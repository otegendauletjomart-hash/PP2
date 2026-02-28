import datetime

current_date = datetime.datetime.now()

yesterday = current_date - datetime.timedelta(days=1)
print(yesterday)

print(current_date)

tomorrow = current_date + datetime.timedelta(days=1)
print(tomorrow)