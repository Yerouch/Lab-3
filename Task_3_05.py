def numeral(num):  # функция для перевода числа в пределах от 1 до 12 в слово, в качестве аргумента число
    if num == 1:
        return "One"
    if num == 2:
        return "Two"
    if num == 3:
        return "Three"
    if num == 4:
        return "Four"
    if num == 5:
        return "Five"
    if num == 6:
        return "Six"
    if num == 7:
        return "Seven"
    if num == 8:
        return "Eight"
    if num == 9:
        return "Nine"
    if num == 10:
        return "Ten"
    if num == 11:
        return "Eleven"
    if num == 12:
        return "Twelve"
    else:
        return ""


def main():  # главная функция
    for i in range(1, 13):
        print(numeral(i))  # вызов функции numeral


if __name__ == "__main__":  # проверка импорта программы
    main()  # вызов функции main в случае, если программа не импортирована
