# Задача:
# https://i.gyazo.com/4179ff77a042afee17c92830a3901ef8.png

# Решение:
# объявление функции
# объявление функции
def is_one_away(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if  word1[i] != word2[i]:
                    count += 1
        if count == 1:
            return True
        else:
            return False
    else:
        return False
# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

# Альтернативное решение (not mine):
# объявление функции
# def is_one_away(word1, word2):
#     return len([i for i in word1 if i not in word2]) == 1 and len(word1) == len(word2)
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))