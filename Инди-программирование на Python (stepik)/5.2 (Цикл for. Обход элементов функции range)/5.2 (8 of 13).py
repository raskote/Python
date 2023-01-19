# Задача:
# https://i.gyazo.com/852472339cfe2f2c62af707d6fc86736.png

# Решение:
s = 0
for i in range (int(input())):
    if i%3==0 or i%5==0:
        s += i
print(s)

# Альтернатива (not mine)
# print(sum(i for i in range(int(input())) if not i % 3 or not i % 5))