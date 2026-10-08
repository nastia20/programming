import datetime
def is_adult(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year

    return age >= 18
