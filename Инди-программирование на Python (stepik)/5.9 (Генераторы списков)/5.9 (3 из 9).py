# Задача:
# https://i.gyazo.com/475f6e6fc36b834084b488860c0f0d9b.png

# Решение:
x = int(input())
li = [i for i in range(1, x+1) if x%i==0]
print(li)