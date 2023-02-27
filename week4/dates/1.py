import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2023, 3, 1)
print(y)

z = datetime.datetime(2023, 10, 23)
print(z.strftime("%B"))