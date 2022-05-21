def hypotenuse(a, b):  # функция для нахождения гипотенузы, в качестве аргументов два числа – катеты
    return pow(a*a + b*b, 0.5)


katet1 = float(input("Введите длину первого катета: "))
katet2 = float(input("Введите длину второго катета: "))
print("Длина гипотенузы:", hypotenuse(katet1, katet2))  # вызов функции hypotenuse
