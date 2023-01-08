# Задача:
# 8. Напишите функцию, которая принимает строку и возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.

# Решение:
s = input()
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 1:
        print(chr(i + 97), letters[i])

# Альтернатива (не очень) (mine):
# x = input().lower()
# for i in x:
#     if x.count(i) > 1:
#         print(i, x.count(i))


# Альтернатива (очень) (not mine):
# s = 'attachment'
# abc = 'qwertyuiopasdfghjklzxcvbnm'
# for i in abc:
#     count = 0
#     for j in s:
#         if j == i:
#             count += 1
#     if count > 1:
#         print(i, 'встречается', count, 'раз')
