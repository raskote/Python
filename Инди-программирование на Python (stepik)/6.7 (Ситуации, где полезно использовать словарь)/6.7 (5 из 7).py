# Задача:
# https://i.gyazo.com/ad6f5efbffdb8c0f19b70d3e886482c6.png

# Решение:
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
for i in input().lower():
    if i.isalpha():
        print(morze[i], end = " ")
    else:
        print(" ", end = "\n")

# Альтернатива (not mine):
# for i in input().lower().split():
#     for j in i:
#         print(morze[j], end=' ')
#     print()