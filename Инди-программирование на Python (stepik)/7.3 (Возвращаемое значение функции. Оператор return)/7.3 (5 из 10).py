# Задание:
# https://i.gyazo.com/4862f97f59d58132dc5ff1306138955a.png

# Решение:
def find_duplicate(lst):
    li = []
    for i in lst:
        if i not in li and li.count(i) == 0 and lst.count(i) > 1:
            li.append(i)
        else:
            continue
    return(li)

assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print('Все успешно')