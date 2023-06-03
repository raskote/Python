# Задание:
# https://i.gyazo.com/272df0744cf3cdba69beebfd62866eac.png

# Решение:
def sum_num(s):
    sum = 0
    for i in s:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            sum += int(i)
    print(sum)

# Альтернатива (not mine):
# def sum_num(s):
#     print(sum([int(i) for i in s if i.isdigit()]))