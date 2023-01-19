# Задача:
# https://i.gyazo.com/627be83492657bf21709f9f6aa6c2d94.png

# Решение:
n = int(input())
i = 1
a = []
while i*i <= n:
    if n%i == 0:
        a.append(i)
        if i!=n//i:
            a.append(n//i)
    i += 1
if len(a) > 2 or n == 1:
    print("No")
else:
    print("Yes")

# Альтернатива (not mine):
# a=int(input())
# i=2
# while a%i!=0 and i<a:
#     i+=1
# print('Yes' if i==a else 'No')