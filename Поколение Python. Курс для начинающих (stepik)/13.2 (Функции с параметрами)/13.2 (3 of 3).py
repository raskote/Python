# Задача:
# https://i.gyazo.com/e7c1ca60765c5e11eb1faf809153c1ce.png

# Решение:
# объявление функции
# объявление функции
def print_digit_sum(num):
    sum = 0
    while num>0:
        sum += num%10
        num //= 10
    print(sum)
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)