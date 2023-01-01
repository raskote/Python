# Задача:
# https://i.gyazo.com/67004f1332ea46f665bd5540a5ae3db1.png

# Решение:
n = int(input())
for i in range(1, n+1):
    x = input().lower()
    if "рок" in x:
        print(i, (x.index("рок")+1))


# Альтернатива (not mine)
# s, expression = "", "РОК"
# for i in range(int(input())):
#     a = input().upper()
#     if a.find(expression) >= 0:
#         s += str(i+1) + ' ' + str(a.index(expression)+1) + '\n'
# print(s)