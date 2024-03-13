from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_until_birthday = (next_birthday - today).days
        if 0 <= days_until_birthday <= 7:
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": next_birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [{"name": "Jane Smith", "birthday": "1990.03.10"},
        {"name": "Nick Darsel", "birthday": "1984.03.11"},
        {"name": "Liam Smith", "birthday": "1995.03.12"},
	{"name": "Mohel Smith", "birthday": "1995.03.13"},
        {"name": "John Dark", "birthday": "1985.03.14"},
        {"name": "Mary Dark", "birthday": "1985.03.15"},
        {"name": "Derek Dark", "birthday": "1985.03.16"},
        {"name": "Jane Smith", "birthday": "1990.03.17"}, 
        {"name": "Liam Smith", "birthday": "1995.03.18"},
	{"name": "Mohel Smith", "birthday": "1995.03.19"},
        {"name": "John Dark", "birthday": "1985.03.20"},
        {"name": "Mary Dark", "birthday": "1985.03.21"},
        {"name": "Derek Dark", "birthday": "1985.03.22"},
        {"name": "Jane Smith", "birthday": "1990.03.23"}]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

