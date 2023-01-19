# Задача:
# https://i.gyazo.com/c34bfd18fefa42de6564095fde72ed67.png

# Решение:
s = ''
for i in range(int(input())):
    a = input()
    if len(a)>10:
        s += str(a[0]) + str(len(a)-2) + str(a[-1]) + '\n'
    else:
        s += str(a) + '\n'
print(s)

# Альтернатива (not mine)
