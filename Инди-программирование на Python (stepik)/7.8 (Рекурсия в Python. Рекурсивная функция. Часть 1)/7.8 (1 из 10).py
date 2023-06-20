# Задание:
# https://i.gyazo.com/74c42ebfaf2f33f7355a07d22b60ada6.png

# Решение:
def print_from(n: int):
    if n != 0:
        print(n)
        print_from(n-1)

print_from(5)