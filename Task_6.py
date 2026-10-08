#Завдання 6: Обчислення факторіала

N = int(input("Введіть ціле додатне число N: "))

factorial = 1

for i in range(1, N + 1):
    factorial *= i

print(f"Факторіал числа {N} дорівнює: {factorial}")