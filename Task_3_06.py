def prime_number(num):  # функция для проверки простоты числа, в качестве аргумента число
    if num < 2:
        return False
    else:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
        return True


def main():  # главная функция
    number = int(input("Введите целое число: "))
    if prime_number(number):  # вызов функции prime_number
        print("Число простое.")
    else:
        print("Число не является простым.")


if __name__ == "__main__":  # проверка импорта программы
    main()  # вызов функции main в случае, если программа не импортирована
