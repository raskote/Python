# Задание:
# https://i.gyazo.com/35be001ae209d4d9ddfbcf7d9af84081.png

# Решение:
year = int(input())
year += 1
while (len(set(str(year)))) != 4:
    year +=1
print(year)





