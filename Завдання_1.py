#Завдання 1: Геометрія прямокутного трикутника
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

D = b**2 - 4 * a * c

if D > 0:

    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    solutions = (x1, x2)
elif D == 0:

    x = -b / (2 * a)
    solutions = (x,)
else:

    solutions = ()

print("solutions =", solutions)