# Задача:
# https://i.gyazo.com/a274741c79c5cf7180479aec011349d1.png

# Решение:
x = int(input())
print(tuple([i for i in range(x, x**2+1) if i%2!=0]))
