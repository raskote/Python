# Задача:
# https://i.gyazo.com/9a2dc7a3bf541bd827d5197adfb28cde.png

# Решение:
# объявление функции
def is_valid_password(password):
    li = password.split(":")
    if len(li) == 3:
        li_int = [int(i) for i in li]
        flag = True
        for j in range(2, (li_int[1]//2)+1):
            if li_int[1] % j == 0:
                flag = False
        return li[0] == li[0][::-1] and li_int[2]%2==0 and flag
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))