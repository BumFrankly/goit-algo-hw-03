from datetime import datetime

def get_days_from_today(date):

  date_obj = datetime.strptime(date, '%Y-%m-%d')

  today = datetime.today()

  difference = today - date_obj
  days_from_today = difference.days

  return days_from_today

date = '2020-10-09'
days_from_today = get_days_from_today(date)
print(f"Количество дней от {date} до сегодня: {days_from_today}")