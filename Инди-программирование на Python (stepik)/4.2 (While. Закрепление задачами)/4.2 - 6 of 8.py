# Задача:
# https://i.gyazo.com/538035dacb1426006fd1a1826774d4ea.png

# Решение:
n = int(input())
square_in_row = 0
count = 0
all_squares = 0
while all_squares <= n:
    count += 1
    square_in_row += count
    all_squares += square_in_row
print(count-1)



