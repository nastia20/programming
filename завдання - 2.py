def create_user(username, role="user", status="active"):

    return f"Користувач: {username}, Роль: {role}, Статус: {status}"

print(create_user("Анастасія"))

print(create_user("Ілля", "admin"))