# Задача:
# https://i.gyazo.com/eb66ad00740bc219ae9c18a57cd44676.png

# Решение:
n = int(input())
a = []
for i in range(1, n+1):
    a.extend(i*str(i).split())
print(*a[:n])

#Альтернатива (not mine):
# i, n, s = 1, int(input()), []
# while len(s) < n:
#     s += [i] * i
#     i += 1
# print(*s[:n])
