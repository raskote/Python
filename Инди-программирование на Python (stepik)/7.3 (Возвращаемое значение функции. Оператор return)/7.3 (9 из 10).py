# Задание:
# https://i.gyazo.com/bfd80af0cbdc3dbe6afca5547787e271.png

# Решение:
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n):
    n = factorial(n)
    count = 0
    for i in reversed(str(n)):
        if i == "0":
            count +=1
        else:
            return count
    return count

# код ниже не стоит удалять, он нужен для проверки
assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print('Проверки пройдены')