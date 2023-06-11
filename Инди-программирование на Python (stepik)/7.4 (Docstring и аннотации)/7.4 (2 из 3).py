# Задание:
# https://i.gyazo.com/843b69235ee61a04b8bd5dd1017b8233.png

# Решение:
def shift_letter(letter: str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"
    if (ord(letter) + shift % 26) <= 122:
        return (chr((ord(letter) + shift % 26)))
    elif (ord(letter) + shift%26) > 122:
        return (chr((ord(letter) + shift%26)-26))
    elif (ord(letter) + shift) < 97:
        return (chr((ord(letter)+26) + shift))

print(shift_letter("w", 28))
print(5%26)

# Альтернатива (not mine):
# def shift_letter(letter: str, shift: int) -> str:
#     "Функция сдвигает символ letter на shift позиций"
#     return chr((ord(letter) - 97 + shift) % 26 + 97)