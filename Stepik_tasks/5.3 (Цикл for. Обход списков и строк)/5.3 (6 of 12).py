# Задача:
# https://i.gyazo.com/7fa9a6f3f4b6ddcb23fab1f6acdf6451.png

# Решение:
n = list(map(int,input().split()))
r = int(input())
count = 0
for i in range(len(n)):
    count += 1
    if n[i] == r:
        print(count)
        break
if r not in n:
    print("ErrorValue")

# Альтернатива_1 (not mine):
# a = input().split()
# b = input()
# for i in range(len(a)):
#     if a[i] == b:
#         print(i+1)
#         break
# else:
#     print('ErrorValue')
