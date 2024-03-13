import re

def normalize_phone(phone_number):

    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)
    
    if all(char == '0' for char in cleaned_number):
        return ""
    
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = "+380" + cleaned_number[3:]
        else:
            cleaned_number = "+380" + cleaned_number.lstrip('0')
    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "50-111-22-22",
    "350 111 22 11   ",
]

raw_numbers = [number.replace('\\t', ' ').replace('\\n', ' ') for number in raw_numbers]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
