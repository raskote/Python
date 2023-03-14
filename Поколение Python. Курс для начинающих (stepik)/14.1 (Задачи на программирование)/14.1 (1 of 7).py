# Задание:
# https://i.gyazo.com/a0da2bb17c4fdf4c15c50c76276fe07d.png

# Решение:
# объявление функции
def draw_triangle():
    n = 8
    for i in range(1,9):
        print((n-i) * " ", end= "")
        print(i * "*", end= "")
        print((i-1) * "*")


# основная программа
draw_triangle()  # вызов функции