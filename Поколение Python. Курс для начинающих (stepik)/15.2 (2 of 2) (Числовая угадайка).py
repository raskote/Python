# Решение:
# Заголовок программы
import random
count = 0
print("Добро пожаловать в числовую угадайку")
range = int(input("Укажите правую границу для случайного выбора числа: "))
num = random.randint(1, range)
# Функция проверки корректности введенных данных

def is_valid(val):
    return 1 <= int(val) <= range

while True:
    print(num)
    n = input(f"Введите число от 1 до {range}: ")
    count += 1
    if not is_valid(n):
        print(f'А может быть все-таки введем целое число от 1 до {range}?')
        continue
    else:
        n = int(n)
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print("Вы угадали, поздравляем!")
            response = input("Запустить новую игру (да/нет): ")
            if response.lower() == "да":
                range = int(input("Укажите правую границу для случайного выбора числа: "))
                num = random.randint(1, range)
                count = 0
                continue
            else:
                print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                print(f"Количество попыток: {count}")
                break

