# Задача:
# https://i.gyazo.com/030666280007f0c1e1b099e6e655715f.png

# Решение:
n, m = map(int, input().split())
li = []
count = 0
for i in range(n):
    row = [i for i in range(m)]
    # for j in range(n):
    #     row.append()
    li.append(row)
print(li)

for i in range(n):
    if i % 2 != 0:
        print(*li[i][::-1])
    else:
        print(*li[i])



# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(a)
#     li.append(row)