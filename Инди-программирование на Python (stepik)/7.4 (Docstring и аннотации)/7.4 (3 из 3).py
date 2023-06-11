# Задание:
# https://i.gyazo.com/10d186fc87f9c58d162f669ccaf1b5cd.png

# Решение:
def shift_letter(letter: str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"
    return chr((ord(letter) - 97 + shift) % 26 + 97)

def caesar_cipher(letter: str, shift: int) -> str:
    "Шифр цезаря"
    s = ""
    for i in letter:
        if i.isalpha():
            s += shift_letter(i, shift)
        else:
            s += i
    return s
