# Задача:
# https://i.gyazo.com/bdeee135e44a0a69fbdf09a9d06b08ef.png

# Решение:
n = input()
count = 0
for i in n:
    if i == ")":
        count -= 1
        if count < 0:
            break
    else:
        count += 1
if count == 0:
    print("YES")
else:
    print("NO")

# Альтернатива_1 (not mine)
# s = input()
# while '()' in s:
#     s = s.replace('()', '')
# print('NO' if s else 'YES')
