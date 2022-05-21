def price(dist):  # функция для нахождения цены поездки на такси, в качестве аргумента число – пройденное расстояние
    return dist//140*extra + base


base = 4
extra = 0.25
distance = int(input("Введите расстояние поездки в метрах: "))
print("Цена поездки: $", price(distance), sep='')  # вызов функции price
