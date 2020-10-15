import calendar
import datetime


def date_converter(date):
    month_names = []
    converted_date = []
    for i in calendar.month_name[1:]:
        i = datetime.datetime.strptime(i, "%B")
        x = datetime.datetime.strftime(i, "%b")
        month_names.append(x.upper())
    month_numbers = [i for i in range(1, 13)]
    months = dict(zip(month_numbers, month_names))
    j = datetime.datetime.strptime(date, "%d-%b-%y")
    y = datetime.datetime.strftime(j, "%Y")
    str_split = date.split("-")
    for k, v in months.items():
        if v == str_split[1]:
            converted_date.append(y)
            converted_date.append(str(k))
            converted_date.append(str_split[0])
    print(tuple(converted_date))


date_converter("8-MAR-85")
