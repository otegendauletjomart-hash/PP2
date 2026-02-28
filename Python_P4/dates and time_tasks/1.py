from datetime import datetime, timedelta

current_date = datetime.now()
print(current_date)

five_days = timedelta(days=5)

new_date = current_date - five_days
print(new_date)