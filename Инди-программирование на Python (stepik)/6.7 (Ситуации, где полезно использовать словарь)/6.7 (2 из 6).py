# Задача:
# https://i.gyazo.com/518d2320bca5fc70c382ac90cdfc012f.png

# Решение:
s = input()
d = {}
for i in s:
    if i.isalpha():
        d[i.lower()] = d.get(i.lower(), 0) + 1
print(d)