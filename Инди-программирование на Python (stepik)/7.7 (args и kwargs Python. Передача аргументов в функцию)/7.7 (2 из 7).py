# Задание:
# https://i.gyazo.com/09ed8def00514599209412a3e4d56f24.png

# Решение:
def check_sum(*args: int):
    sum = 0
    for i in [*args]:
        sum += i
    print("not enough" if sum < 50 else "verification passed")

# Альтернатива (not mine):
# def check_sum(*args):
#     print('not enough' if sum(args)<50 else 'verification passed')