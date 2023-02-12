import calendar
year =int(input("Enter year:"))
for i in range(1,12):
    month = i
    x = calendar.month(year, month)
    print(x)
