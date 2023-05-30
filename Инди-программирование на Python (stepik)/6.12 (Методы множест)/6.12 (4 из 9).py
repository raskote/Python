# Задание:
# https://i.gyazo.com/36cc26ac353ce21bb6b853b1ebc6a062.png

# Решение:
n = int(input())
x = set(list(map(int, input().split())))
for i in range(n-1):
    li = map(int, input().split())
    x.update(li)
print(len(x))

# Альтернатива_1 (not mine):
# my_set = set()
# for i in range(int(input())):
#     my_set.update(input().split())
# print(len(my_set))

# Альтернатива_2 (not mine):
# print(len({i for _ in range(int(input())) for i in input().split()}))