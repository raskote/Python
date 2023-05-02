# Задача:
# https://i.gyazo.com/980efb946aedeccd3e7960f6c35d4915.png

# Решение:
r, c = map(int, input().split())
main_count, count, sub_count, count2 = 0, 0, 0, 0
li = [list(input()) for c in range(r)]
for i in range(r):
    main_count += count
    count = 0
    for j in range(c):
        if li[i].count('S'):
            count = 0
            break
        elif li[i][j] == ".":
            count += 1
            li[i][j] = "!"
main_count += count

for q in range(c):
    sub_count += count2
    count2 = 0
    for w in range(r):
        if li[w][q] == "S":
            count2 = 0
            break
        elif li[w][q] not in ["S", "!"]:
            li[w][q] = '?'
            count2 +=1
sub_count += count2
print(main_count + sub_count)