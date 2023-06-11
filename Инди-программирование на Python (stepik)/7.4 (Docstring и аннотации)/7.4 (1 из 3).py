# Задание:
# https://i.gyazo.com/41b9b877bb2788937eb6d86e9721ee9f.png

# Решение:
def first_repeated_word(s: str) -> str:
    "Находит первый дубль в строке"
    li = []
    s = s.split()
    for i in s:
        if i not in li:
            li.append(i)
        elif i in li:
            return i
