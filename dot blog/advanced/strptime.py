# from datetime import datetime as dt

# date_value = dt.strptime('2018/06/25 10:30:00', '%Y/%m/%d %H:%M:%S')
# print(date_value)

# from datetime import datetime as dt

# date_value = dt.strptime('26/06/2018 2:20:00 PM', '%d/%m/%Y %I:%M:%S %p')
# print(date_value)

from datetime import datetime as dt

date_value = dt.strptime('2018-06-27T11:28:54', '%Y-%m-%dT%H:%M:%S')
print(date_value)
