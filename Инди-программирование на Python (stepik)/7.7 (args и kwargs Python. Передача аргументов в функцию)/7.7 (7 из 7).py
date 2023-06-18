# Задание:
# https://i.gyazo.com/d0f0d748843b5dfe1714494942f7bcab.png

# Решение:
def create_actor(**kwargs):
    base_kwargs = {'name': 'Райан', 'surname': 'Рейнольдс', 'age': 46}
    base_kwargs.update(kwargs)
    return base_kwargs


