from datetime import datetime
from operator import mod

input_list = [2017, 8, 2, 2018, 1, 1]
dateStart = str(input_list[0]) + '-' + str(input_list[1]) + '-' + str(input_list[2])
dateEnd = str(input_list[3]) + '-' + str(input_list[4]) + '-' + str(input_list[5])

dateStart_month = datetime.strptime(dateStart, "%Y-%m-%d").month
dateEnd_month = datetime.strptime(dateEnd, "%Y-%m-%d").month

print(dateStart_month)
print(dateEnd_month)

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']

resultant = list(zip(months, names))

print(list(zip(months, names)))

months_reqd = []
diff = abs(dateEnd_month - dateStart_month)
print(diff)
if dateEnd_month < dateStart_month:
    dateEnd_month += 12
range_of_months = range(dateStart_month, dateEnd_month + 1)
res_list = list(map(lambda x: mod(x, 12), range_of_months))
print(res_list)
for item in resultant:
    if item[0] in res_list:
        months_reqd.append(item[1])
print("Final list of months: ", months_reqd)
