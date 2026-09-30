from string import printable
from random import choice

def settings_func()->dict:#собирает настройки для пароля
    setting = {}

    lower_case = input("Наличие нижнего регистра в пароле (Y/N): ").upper()
    upper_case = input("Наличие верхнего регистра в пароле (Y/N): ").upper()
    simvols = input("Специальные символы, например #%@ и т.д. (Y/N): ").upper()
    length_pass = int(input("Длина пароля (до 100 символов) : "))

    if lower_case == "Y":setting["lower"] = 1

    if upper_case == "Y":setting["upper"] = 1

    if simvols == "Y":setting["simv"] = 1

    if length_pass < 0 or length_pass > 100:setting["length"] = 10
    else:
        setting["length"] = length_pass

    return setting

def generate_password(settings:dict)->str:
    data = {}
    password = ""

    if len(settings) > 1:                 #делаем проверку исходя из прошлой функции (если пользователь 3 раза ввёл N то будет ошибка)
        for key,value in settings.items():  #создаём словарь откуда будем брать символы для пароля
            if key == "lower":
                data["lower_case"] = printable[10:36]

            elif key == "upper":
                data["upper_case"] = printable[10:36].upper()

            elif key == "simv":
                data["simvols"] = "-+*@!?#/_.%$()="

            elif key == "length":
                length_pass = settings["length"]

        while len(password) != length_pass:
            random_sim = choice(choice(list(data.values())))  #сначала берём случайный список ключей например "abcd...." и затем ещё один choice берёт 1 случайный символ
            password += random_sim
            
        print(f"Ваш пароль {password}")

    else:print("Неверный ввод: Недостаточно символов для создания пароля")         #вывод при неправильном вводе

generate_password(settings_func())
    