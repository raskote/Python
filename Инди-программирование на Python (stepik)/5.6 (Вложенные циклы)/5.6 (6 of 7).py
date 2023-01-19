# Задача:
# https://i.gyazo.com/9bbd9caf4c852c66cbaa83e352a55457.png

# Решение:
n = int(input())
l = list(map(int, input().split()))
count = 0
for i in range(n-1):
    for j in range(n-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            count += 1
print(*l)
print(count)
