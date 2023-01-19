# Задача:
# https://i.gyazo.com/a28a369a31842d0913d7ff75f34bf44a.png

# Решение:
word = input()
i = 0
while len(word) != i:
    if word[i] == "e" or word[i] == "a":
        print("Ага! Нашлась")
        break
    print("Текущая буква:", word[i])
    i += 1
else:
    print("Распечатали все буквы")

# Альтернатива (not mine)
