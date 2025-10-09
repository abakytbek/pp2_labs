from datetime import datetime, timedelta

current = datetime.now()
new_date = current - timedelta(days=5)

print("Today:", current.strftime("%Y-%m-%d"))
print("5 days ago:", new_date.strftime("%Y-%m-%d"))
