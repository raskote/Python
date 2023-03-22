# Задание:
# https://i.gyazo.com/a24d895d30df57d616853253f6763135.png

# Решение:
string = input()
start_up = ord('A')
start_low = ord('a')
result = ""
word = ""
count = len(string)
li = []
for i in string:
    if i.isalpha():
        word += i
    if not i.isalpha():
        li.append(word)
        li.append(i)
        word = ""
    count -= 1
    if count == 0:
        li.append(word)
for j in li:
    for k in j:
        if not k.isalpha():
            result += k
        elif k.isupper():
            result += chr((ord(k) - start_up + len(j)) % 26 + start_up)
        elif k.islower():
            result += chr((ord(k) - start_low + len(j)) % 26 + start_low)
print(result)