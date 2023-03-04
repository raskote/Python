# Задача:
# https://i.gyazo.com/44615fa46beba45adef533b31dd5353e.png

# Решение:
# объявление функции
def draw_triangle(fill, base):
    for i in range(int(base/2)+1):
        print((i+1)*fill)
    for i in range(int(base/2)):
        print((int(base/2)-i)*fill)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
