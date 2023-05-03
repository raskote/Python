# Задача:
# При помощи генератора-списков создайте список, состоящий из слов,  начинающихся с буквы 't' или 'T'. Слова возьмите из переменной phrase, также не забывайте про метод split()
# В качестве ответа выведите полученный список, слова в нем должны стоять в том же порядке, в котором они стояли в изначальной фразе
# phrase = 'Take only the words that start with t in this sentence'

# Решение:
phrase = 'Take only the words that start with t in this sentence'
print([i for i in phrase.split() if i.lower().startswith('t')])
