# Задача:
# https://i.gyazo.com/23bc6c1e538a6c37bff921eafbe367e7.png

# Решение:
s, expression = [], "соль"
for i in range(int(input())):
    a = input()
    if expression not in a:
        s.append(a)
print(', '.join(s))

# Альтернатива (not mine)
