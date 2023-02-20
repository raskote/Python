# Задача:
# https://i.gyazo.com/1101cef9542f298d4e07572e2eac4970.png


# Решение:
n = input().strip('#')
li = []
for i in range(int(n)):
    s = input()
    if s.count("#") != 0:
        for j in range(len(s)):
            for t in range(len(s[j])):
                if "#" in s[j][t]:
                    li.append(s[0:j].rstrip())
    else:
        li.append(s)

for k in range(len(li)):
    print(li[k])

# Решение (not mine):
# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())