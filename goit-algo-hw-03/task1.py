from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Неправильний формат дати. Потрібно YYYY-MM-DD.")
        return None

    today = datetime.today()

    difference = today - date_obj
    days_from_today = difference.days

    return days_from_today

date = '2020-10-09'
days_from_today = get_days_from_today(date)
if days_from_today is not None:
    print(f"Кількість днів від {date} до сьогодні: {days_from_today}")
