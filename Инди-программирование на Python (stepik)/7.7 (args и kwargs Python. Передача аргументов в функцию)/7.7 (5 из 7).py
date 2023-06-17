# Задание:
# https://i.gyazo.com/fad53410e99343f9171083e15229eada.png

# Решение:
def print_goods(*args):
    li = [i for i in args if type(i) == str and len(i) != 0]
    if li:
        for i in li:
            print(f'{li.index(i)+1}. {i}')
    else:
        print("Нет товаров")
#
# Альтернатива (not mine):
# def print_goods(*args):
#     s = [i for i in args if isinstance(i, str) and len(i)]
#     [print(f'{i}. {j}') for i, j in enumerate(s, start=1)] if s else print('Нет товаров')