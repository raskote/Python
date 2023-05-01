# Задача:
# https://i.gyazo.com/8fc7cb9a3d51e70785800ca2748ff0a9.png

# Решение:
n = int(input()) # инициализируем число - предел строк и столбцов квадратной матрицы
li = []  # объявляем пустой список
start = 0  # объявляем переменную старта в периоде
end = n
count = 1
m = n - 1
# создаем матрицу, заполняемую последовательностью цифр от 0 до последней в пределе матрицы
for k in range(n):
    row = [0 for m in range(n)]
    li.append(row)
# проходимся по уже созданной матрице и меняем числа в соответствии с условиями задачи
while n > 0:
    # верх
    for i in range(start, n):
        for j in range(start, n - 1):
            if i == start:
                li[i][j] = count
                count += 1
    # право
    for i in range(start, n - 1):
        for j in range(start, n):
            if j + 1 == n:
                li[i][j] = count
                count += 1
    # низ
    for i in range(start, n):
        for j in range(start, n):
            if i + 1 == n:
                li[i][m-j] = count
                count += 1
    # лево
    for i in range(start+1, n - 1):
        for j in range(start, n):
            if j == start:
                li[m - i][j] = count
                count += 1
    start += 1
    n -= 1
# выводим построчно матрицу
for i in range(len(li)):
    print(*li[i])

