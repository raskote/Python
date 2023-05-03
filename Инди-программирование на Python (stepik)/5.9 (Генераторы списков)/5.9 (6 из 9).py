# Задача:
# Создайте список первых букв каждого слова из строки st и выведите его на экран
# st = 'Create a list of the first letters of every word in this string'

# Решение:
st = 'Create a list of the first letters of every word in this string'
print([i[0:1] for i in st.split()])
