# Решение:
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
new_chars = ''



need_digits = input("Включать ли цифры 0123456789? (да/нет) ")
upper_alph = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (да/нет) ")
lower_alph = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz (да/нет) ")
symbols = input("Включать ли символы !#$%&*+-=?@^_ (да/нет) ")
specials = input("Исключать ли неоднозначные символы il1Lo0O (да/нет) ")

if need_digits.lower() == "да":
    chars += digits
if upper_alph.lower() == "да":
    chars += uppercase_letters
if lower_alph.lower() == "да":
    chars += lowercase_letters
if symbols == "да":
    chars += punctuation
if specials == "да":
    for i in chars:
        if i in 'il1Lo0O':
            continue
        else:
            new_chars += i
print(new_chars)

length = int(input("Длина пароля? "))
count = int(input("Сколько паролей нужно для генерации? "))

def generate_password(len, chars):
    password = ''
    for j in range(length):
        password += random.choice(new_chars)
    return password

for i in range(count):
    print(generate_password(length, new_chars))