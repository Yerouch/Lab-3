import Task_3_08
import Task_3_09


secure_password = ""
attempt = 0
while not Task_3_09.password_check(secure_password):  # вызов функции password_check для проверки надёжности пароля
    secure_password = Task_3_08.password()  # вызов функции password для генерации пароля
    attempt += 1
print("Ваш надёжный пароль:", secure_password, "\nКоличество попыток при создании:", attempt)
