from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
  upcoming_birthdays = []
  today = datetime.today().date()

  for user in users:
    birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    birthday_next_year = birthday_this_year.replace(year=today.year + 1)

    days_until_birthday = (birthday_this_year - today).days
    if days_until_birthday < 0:
      days_until_birthday = (birthday_next_year - today).days

    if days_until_birthday <= 7:
      congratulation_date = birthday_this_year

      if birthday_this_year.weekday() == 5: 
        congratulation_date += timedelta(days=2) 

      upcoming_birthdays.append({
        "name": user["name"],
        "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
      })

  return upcoming_birthdays

users = [
  {"name": "Олена", "birthday": "2024.03.13"},
  {"name": "Вікторія", "birthday": "2024.03.16"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:", upcoming_birthdays)
