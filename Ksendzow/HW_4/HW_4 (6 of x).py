# Задача:
# 6. Сравнить 2 строки без учёта регистра
# ==============================

# Решение:
str_1, str_2 = input().lower(), input().lower()
if str_1 == str_2:
    print(True)
else:
    print(False)
