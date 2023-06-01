# Задание:
# https://i.gyazo.com/1aac1d297b150f839747224065b50979.png

# Решение:
set_a = input()
set_b = set()
set_c = set()

for i in set_a:
    if i.isdigit() and i not in set_b:
        set_b.add(i)
    elif i in set_b:
        set_c.add(i)
if set_c:
    print(*sorted(set_c))
else:
    print("NO")


