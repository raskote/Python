# Задание:
# https://i.gyazo.com/f4457ee414576d5d74cc367968cd1a3d.png

# Решение:
def is_pangram(text):
    azb = [chr(a) for a in range(97, 123)]
    text = text.lower().replace(" ", "")
    for i in azb:
        if i not in text:
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))