# Задание:
# https://i.gyazo.com/4fa4d0dc9c36325bee2701a1c08dc75e.png

# Решение:
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

n = int(input())
li = []
li2 = []
for i in range(n):
    li.append(int(input()))
for i in range(1, len(li)):
    li2.append(gcd((sorted(li))[0], li[i]))
print(min(li2))