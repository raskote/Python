# Задача:
# https://i.gyazo.com/425363301364e519b5fa478131c54c1b.png

# Решение:
n = int(input())
# # n = 734573659783465783465978346593487
# n = 192
count = 0
count_new = 0
count_new_new = 0
while n > 0:
    last_digit = n % 10
    count += last_digit
    n = n // 10
    while n == 0 and count > 0:
        last_digit_new = count % 10
        count_new += last_digit_new
        count = count // 10
        while count == 0 and count_new > 0:
            last_digit_new_new = count_new % 10
            count_new_new += last_digit_new_new
            count_new = count_new // 10
print(count_new_new)

# Альтернатива (not_mine)
# number = int(input())
# total = 0
# while number > 9:
#     while number != 0:
#         total += number % 10
#         number //= 10
#     number, total = total, 0
# print(number)
