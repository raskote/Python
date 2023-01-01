# Задача:
# https://i.gyazo.com/89fc9b4419b00f28076153fa31a8c71f.png

# Решение:
a,b = int(input()), int(input())
for i in range (a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

# Альтернатива (not mine)
# for n in range(int(input()), int(input()) + 1):
#     print('Fizz' * (not n % 3) + 'Buzz' * (not n % 5) or n)