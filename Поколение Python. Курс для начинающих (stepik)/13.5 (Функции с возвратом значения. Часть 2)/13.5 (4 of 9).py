# Задача:
# https://i.gyazo.com/b6a0ac995b5effb0fb652e39ae75180b.png

# Решение:
# объявление функции
def is_password_good(password):
    if len(password) >= 8:
        count, count1, count2, count3 = 0, 0, 0, 0
        for i in password:
            if i.isupper():
                count1 += 1
            elif i.islower():
                count2 += 1
            elif i.isdigit():
                count3 += 1
    else:
        return False
    if count1:
        count +=1
    if count2:
        count +=1
    if count3:
        count +=1
    if count == 3:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

# Альтернативное решение (not mine):
# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])
#
#
# txt = input()
# print(is_password_good(txt))