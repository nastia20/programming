#Завдання 8: Перестановка сусідів у масиві
data = input("Введіть елементи через пробіл: ").split()
for i in range(0, len(data) - 1, 2):
    temp = data[i]
    data[i] = data[i + 1]
    data[i + 1] = temp
print("Вивід:", *data)