# Задача:
# https://i.gyazo.com/e2483bb6e9106a52119d1b44701f9ba7.png

# Решение:
n = input()
stek = []
count = 0
for i in n:
    if i == "(" or i == "{" or i == "[":
        stek.append(i)
    if i == ")" or i == "}" or i == "]":
        if len(stek) != 0:
            if stek[-1] + i == "()" or stek[-1] + i == "[]" or stek[-1] + i == "{}":
                stek.pop(-1)
            else:
                count += 1
                print("NO")
                break
        else:
            count += 1
            print("NO")
            break
if len(stek) == 0 and count == 0:
    print("YES")
elif len(stek) != 0 and count == 0:
    print("NO")

# Альтернатива_1 (not mine)

