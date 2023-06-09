# Задание:
# https://i.gyazo.com/26a179455f67341d3f1e7696b96c65d2.png

# Решение:
def first_unique_char(s):
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1

s = input()
print(first_unique_char(s))