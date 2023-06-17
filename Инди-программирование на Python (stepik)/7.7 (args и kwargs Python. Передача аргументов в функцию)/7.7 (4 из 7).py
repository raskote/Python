# Задание:
# https://i.gyazo.com/8be703f8cca12e3025353805eb89a7ed.png

# Решение:
def only_one_positive(*args: int):
    li = [i for i in args if i > 0]
    return True if len(li) == 1 else False
