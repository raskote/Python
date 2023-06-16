# Задание:
# https://i.gyazo.com/a533daa5dac14da390435faeec71a2ce.png

# Решение:
def replace(text: str, old: str, new: str = ''):
    for i in text:
        if i == old:
            text = text.replace(i, new)
    return text