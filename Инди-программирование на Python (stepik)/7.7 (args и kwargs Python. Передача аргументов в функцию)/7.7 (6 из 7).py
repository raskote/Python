# Задание:
# https://i.gyazo.com/503b380b56fe9fb87fa764badb103e1d.png

# Решение:
def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

print(info_kwargs(first_name="John", last_name="Doe", age=33))