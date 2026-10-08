import random
def get_daily_discount():

    chance = random.randint(1, 100)

    if 1 <= chance <= 10:
        return "Ваша знижка: 50%"
    elif 11 <= chance <= 30:
        return "Ваша знижка: 20%"
    else:
        return "Ваша знижка: 5%"
