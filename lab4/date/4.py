from datetime import datetime

d1 = datetime.strptime('2023-01-02 00:12:10', '%Y-%m-%d %H:%M:%S')
d2 = datetime.now()
timedelta = d2 - d1
print(print("Seconds :",timedelta.days * 24 * 3600 + timedelta.seconds))
