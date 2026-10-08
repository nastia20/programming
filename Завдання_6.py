#Завдання 6: Валідатор паролів (Аналіз рядків у циклі)
password = input("Write password:")

has_lower = False
has_upper = False
has_digit = False

for char in password:
    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True

if has_lower and has_upper and has_digit:
    print("Password is secure")
else:
    print("Password is insecure")