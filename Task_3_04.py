def median(a, b, c):  # функция для нахождения среднего из трёх чисел, в качестве аргументов три числа
    if (a < b < c) or (a > b > c):
        return b
    elif (a < c < b) or (a > c > b):
        return c
    else:
        return a


print("Введите три числа:\n")
num1 = int(input())
num2 = int(input())
num3 = int(input())
print("Медиана введённых чисел:", median(num1, num2, num3))  # вызов функции
