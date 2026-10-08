import random

def assign_moderator(user_list):
    chosen_user = random.choice(user_list)
    return chosen_user
employees = ["Ілля", "Марія", "Іван"]
moderator = assign_moderator(employees)
print(f"Сьогодні коментарі перевіряє: {moderator}")