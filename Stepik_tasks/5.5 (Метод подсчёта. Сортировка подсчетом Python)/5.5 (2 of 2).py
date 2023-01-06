# Задача:
# https://i.gyazo.com/6b2f91f4daa4e2d9da33a8e8136fcd1a.png

# Решение:
x = int(input())
n = []


y = max(n) + 1
count = [0] * y
for i in n:
    count[i] += 1
for i in range(y):
    if count[i] > 0:
        print(i, count[i])

# Альтернатива (not mine):
n = list(map(int,input().split()))
n.sort()
for i in range(len(n)):
    if n[0] <= 0:
        n.pop(0)
if len(n) > 0:
    print(n[0])
else:
    print("Empty")

s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97) * letters[i], end="")