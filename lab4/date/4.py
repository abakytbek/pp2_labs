from datetime import timedelta, datetime

now = datetime.now()
past = now - timedelta(days=1)
diff = (now - past).total_seconds()
print("Date now:", now)
print("Past date:", past)
print("Difference between dates:", diff)