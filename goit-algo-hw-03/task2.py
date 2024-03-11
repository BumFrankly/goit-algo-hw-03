from random import randint

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

  if min < 1 or max > 100:
    return 
  if quantity < 1 or quantity > max - min + 1:
    return 

  lottery_numbers = set() 
  while len(lottery_numbers) < quantity:
    lottery_numbers.add(randint(min, max))

  return sorted(lottery_numbers)

min_value = 2
max_value = 99
quantity_of_numbers = 5
numbers = get_numbers_ticket(min_value, max_value, quantity_of_numbers)

print(f"Переможці: {numbers}")