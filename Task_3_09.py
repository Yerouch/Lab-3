def password_check(word):  # функция для проверки надёжности пароля, в качестве аргумента строка
    uppercase = False
    lowercase = False
    number = False
    if len(word) >= 8:  # проверка на достаточность длины пароля
        for i in range(len(word)):
            if ord(word[i]) in range(65, 90):  # проверка на наличие заглавной буквы в пароле
                uppercase = True
            if ord(word[i]) in range(97, 122):  # проверка на наличие строчной буквы в пароле
                lowercase = True
            if ord(word[i]) in range(48, 57):  # проверка на наличие цифры в пароле
                number = True
        if uppercase and lowercase and number:
            return True
        else:
            return False
    else:
        return False


def main():  # главная функция
    inserted = input("Введите пароль для проверки его надёжности:\n")
    if password_check(inserted):  # вызов функции password_check
        print("Пароль надёжный.")
    else:
        print("Пароль ненадёжный.")


if __name__ == "__main__":  # проверка импорта программы
    main()  # вызов функции main в случае, если программа не импортирована
