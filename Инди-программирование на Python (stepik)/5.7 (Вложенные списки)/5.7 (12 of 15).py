# Задача:
# https://i.gyazo.com/92eeb788508ee4e447065cb56debded8.png

# Решение:
n, m = map(int, input().split())
li = [list(map(int, input().split())) for i in range(n)]
max_num = [max(i) for i in li] # определяем максимальные числа в подстроках
maxx_num = max([i for i in max_num]) # определяем самое максимальное число в списке
print(max_num.count(maxx_num))

