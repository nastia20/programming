#Завдання 7: Статистика (Дисперсія та Стандартне відхилення)
data = [13.1, 19.3, 16.3, 12.9, 14.0, 17.1]
m = len(data)

total_sum = 0
for x in data:
    total_sum += x
mean = total_sum / m

variance_sum = 0
for x in data:
    variance_sum += (x - mean) ** 2
variance = variance_sum / (m - 1)

std_deviation = variance**0.5

print(mean)
print(variance)
print(std_deviation)