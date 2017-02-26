import datetime


def print_heading():
    print('-------------------------')
    print('     Birthday App')
    print('-------------------------')
    print()


def get_birthday_from_user():
    print('When is your birthday?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    bday = datetime.datetime(year, month, day)
    return bday


def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_bday_information(days):
    if days < 0:
        print('Your birthday is in {} days'.format(-days))
    elif days > 0:
        print('Your birthday was {} days ago'.format(days))
    else:
        print('Happy birthday')


def main():
    print_heading()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_bday_information(number_of_days)


main()
