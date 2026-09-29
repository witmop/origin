from string import printable

text = input("Введите слово: ")
change = int(input("Введите сдвиг: "))

if 65 <= ord(text[0]) <= 90 or 97 <= ord(text[0]) <= 122:#определяем по символам unicode какой алфавит будем использовать
    alphabet = printable[10:36]
else:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

pattern = [el.isupper() for el in text]#ищем большие буквы и запоминаем, так будет проще вместо того чтобы делать 2 алфавита маленьких и больших букв и путаться

if change >= len(alphabet):# подготавливаем сдвиг, чтобы он был не больше длины алфавита
        while change >= len(alphabet):
            change -= len(alphabet)

def encryption(string:str,change:int)->str:
    string = string.lower()
    result_string = ""
    temp = ""
    for el in string:
        if (change+alphabet.find(el))>len(alphabet)-1:
            temp+=alphabet[change+alphabet.find(el)-len(alphabet)]
        else:
            temp += alphabet[change+alphabet.find(el)]
    for ind,res in enumerate(pattern):
        if res == True:
            result_string += temp[ind].upper()
        else:
            result_string += temp[ind]
    return result_string
def decryption(string:str,change:int)->str:
    string = string.lower()
    temp = ""
    result_string = ""
    for el in string:
        temp += alphabet[alphabet.find(el)-change]
    for ind,res in enumerate(pattern):
        if res == True:
            result_string += temp[ind].upper()
        else:
            result_string += temp[ind]
    return result_string

print(encryption(text,change))
print(decryption(encryption(text,change),change))

