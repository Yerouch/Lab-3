import random


def password():  # функция для генерации случайного пароля из символов в диапазоне от 33 до 126 в ASCII
    length = random.randint(7, 10)
    word = ""
    for i in range(length):
        word += chr(random.randint(33, 126))
    return word


def main():  # главная функция
    print("Ваш пароль:", password())  # вызов функции password


if __name__ == "__main__":  # проверка импорта программы
    main()  # вызов функции main в случае, если программа не импортирована
