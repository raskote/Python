# Задача:
# https://i.gyazo.com/977670ed9523a07d568437d82a54e522.png

# Решение:
# li1 = ['язык python прекрасен', 'C# - отличный язык программирования', 'Stepik - отличная платформа', 'BEEGEEK FOREVER!', 'язык python появился 20 февраля 1991']
# li2 = ['язык', 'python']
li1 = []
li2 = []
n = int(input())
for i in range(n):
    x = input().lower()
    li1.append(x)

k = int(input())
for j in range(k):
    y = input().lower
    li2.append(y)
li3 = []
for p in range(len(li1)):
    count = 0
    for l in range(len(li2)):
        if li2[l] in li1[p]:
            count += 1
        if len(li2) == count:
            li3.append(li1[p])
print(li3)

#Решение (not mine)
# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)