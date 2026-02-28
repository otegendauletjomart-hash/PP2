from datetime import datetime

date1 = datetime(2026, 2, 28, 12, 0, 0) 
date2 = datetime(2026, 2, 27, 8, 30, 0)  

difference = date1 - date2

seconds = difference.total_seconds()

print(seconds)