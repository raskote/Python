# Решение:
start_en_lower = ord('a')
start_en_upper = ord('A')
start_ru_lower = ord('а')
start_ru_upper = ord('А')

answer = ''
vector = input("Что мы делаем - шифруем (ш) или дешифруем (д)? (ш/д) ")
language = input("Какой язык: EN или RU? ")
key = int(input("Шаг сдвига? "))



if vector.lower() == "ш":
    s = input("Введите фразу для шифрования: ")
    if language.lower() == "en":
        for i in s:
            if not i.isalpha():
                answer += i
            elif i.islower():
                answer += chr((ord(i) - start_en_lower + key) % 26 + start_en_lower)
            elif i.isupper():
                answer += chr((ord(i) - start_en_upper + key) % 26 + start_en_upper)
        print(answer)
    elif language.lower() == "ru":
        for j in s:
            if not j.isalpha():
                answer += j
            if j.islower():
                answer += chr((ord(j) - start_ru_lower + key) % 32 + start_ru_lower)
            elif j.isupper():
                answer += chr((ord(j) - start_ru_upper + key) % 32 + start_ru_upper)
        print(answer)
elif vector.lower() == "д":
    s = input("Введите фразу для дешифрования: ")
    if language.lower() == "en":
        for i in s:
            if not i.isalpha():
                answer += i
            elif i.islower():
                answer += chr((ord(i) - start_en_lower - key) % 26 + start_en_lower)
            elif i.isupper():
                answer += chr((ord(i) - start_en_upper - key) % 26 + start_en_upper)
        print(answer)
    elif language.lower() == "ru":
        for j in s:
            if not j.isalpha():
                answer += j
            elif j.islower():
                answer += chr((ord(j) - start_ru_lower - key) % 32 + start_ru_lower)
            elif j.isupper():
                answer += chr((ord(j) - start_ru_upper - key) % 32 + start_ru_upper)
        print(answer)
