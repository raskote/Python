# Задание:
# https://i.gyazo.com/774f78488d4bb44b3a61eda3de26f113.png

# Решение:
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
print(*sorted(set_a.intersection(set_b)))



