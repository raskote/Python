# Задача:
# https://i.gyazo.com/4191b886540658f63cb5266133b1b45e.png

# Решение:
s1, s2 = input().lower(), input().lower()
d1, d2 = {}, {}
for i in s1:
    d1[i] = d1.get(i, 0) + 1
for i in s2:
    d2[i] = d2.get(i, 0) + 1
print("YES" if d1 == d2 else "NO")

# Альтернатива (not mine):
# print('YES' if sorted(input()) == sorted(input()) else 'NO')