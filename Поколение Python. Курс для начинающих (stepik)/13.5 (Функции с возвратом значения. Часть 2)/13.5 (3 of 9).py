# Задача:
# https://i.gyazo.com/02c3c3744a5d58d8a9a02edea09adf7f.png

# Решение:
# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# объявление второй функции
def get_next_prime(num):
    while True:
        num += 1
        if is_prime(num) == True:
            return num
        else:
            continue


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
