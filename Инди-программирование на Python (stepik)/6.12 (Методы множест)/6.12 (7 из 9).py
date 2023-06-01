# Задание:
# https://i.gyazo.com/097223d8ff53dc4b659d01f86f343736.png

# Решение:
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
print(*sorted(set_a.difference(set_b)))



