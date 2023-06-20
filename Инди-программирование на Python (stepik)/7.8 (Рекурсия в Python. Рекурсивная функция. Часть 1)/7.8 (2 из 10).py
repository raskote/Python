# Задание:
# https://i.gyazo.com/849cd78dae8b5ae769581acef3c8b8cd.png

# Решение:
def print_to(n: int) -> None:
        if n > 0:
                print_to(n-1)
                print(n)

print_to(5)