# Задание:
# https://i.gyazo.com/e547ca0773e5a31faad820961890caad.png

# Решение:
def generate_fizz_buzz_list(n):
    li = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            li.append("FizzBuzz")
        elif i %3 == 0:
            li.append("Fizz")
        elif i %5 == 0:
            li.append("Buzz")
        else:
            li.append(i)
    return li
