# Задача:
# https://i.gyazo.com/201d739d33a91f2c484ae3b09f6b72a7.png

# Решение:
# объявление функции
def is_palindrome(text):
    s = ""
    for i in text:
        if i in (" ", ",", ".", "!", "?", "-"):
            continue
        else:
            s += i
    x = s.lower()[::-1]
    return s.lower() == x
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))