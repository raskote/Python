# Задача:
# https://i.gyazo.com/745c4039caa65790b0358d9472e18696.png

# Решение:

# Заголовок программы
import random
num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку")

# Функция проверки корректности введенных данных
def is_valid(val):
    if 1<= int(val) <= 100:
        return True
    else:
        return False

print(is_valid(101))
