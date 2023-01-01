# Задача:
# https://i.gyazo.com/e93b38a9348d376915f436f4e1de81a2.png

# Решение:
n = int(input())
count_m = 0
count_c = 0
for i in range(n):
    m, c = map(int, input().split())
    if m > c:
        count_m += 1
    elif c > m:
        count_c += 1
    else:
        continue
if count_m > count_c:
    print("Mishka")
elif count_m < count_c:
    print("Chris")
else:
    print("Friendship is magic!^^")

# Альтернатива (not mine)
# n = int(input())
#
# x = y = 0
# for _ in range(n):
#     a, b = input().split()
#     x += int(a > b)
#     y += int(a < b)
#
# print('Mishka' if x > y else 'Chris' if x < y else 'Friendship is magic!^^')