# Задача:
# https://i.gyazo.com/b95e3ed45b4256280fd3c9caf5c33729.png

# Решение:
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
    print(s[i] * "+")


