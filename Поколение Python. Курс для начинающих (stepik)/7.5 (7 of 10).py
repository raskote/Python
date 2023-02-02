# Задача
# https://i.gyazo.com/320a9c4d06aaf1de1af976307110a57e.png

# Решение:
x = 7820
flag = True
while len(str(x)) != 1:
    if x%10 > x//10%10:
        flag = False
    x = x//10
if flag == False:
    print("NO")
else:
    print("YES")
