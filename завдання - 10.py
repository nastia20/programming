import random
import datetime
def generate_ticket(passenger, destination):
    seat = random.randint(1, 50)

    current_date = datetime.datetime.now().date()
    return f"Квиток: {passenger}, Напрямок: {destination}, Місце: {seat}, Дата: {current_date}"

