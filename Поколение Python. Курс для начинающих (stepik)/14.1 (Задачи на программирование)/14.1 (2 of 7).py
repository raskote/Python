# Задание:
# https://i.gyazo.com/c369f7d43f53b6168672f7901546d873.png

# Решение:
def get_shipping_cost(quantity):
    if quantity > 0:
        sum = 1000
        quantity -= 1
        while quantity > 0:
            quantity -= 1
            sum += 120
    return sum

# Альтернативное решение (not mine):
# def get_shipping_cost(quantity):
#     return 1000 + (quantity - 1) * 120
# n = int(input())
# print(get_shipping_cost(n))

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
