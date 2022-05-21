import Task_3_06


def next_prime(num):  # функция для поиска ближайшего из следующих простых чисел, в качестве аргумента число
    while not Task_3_06.prime_number(num):  # вызов функции prime_number из импортированного файла
        num += 1
    return num


def main():  # главная функция
    number = int(input("Введите целое число: "))
    print("Ближайшее из следующих простых чисел:", next_prime(number+1))  # вызов функции next_prime


if __name__ == "__main__":  # проверка импорта программы
    main()  # вызов функции main в случае, если программа не импортирована
