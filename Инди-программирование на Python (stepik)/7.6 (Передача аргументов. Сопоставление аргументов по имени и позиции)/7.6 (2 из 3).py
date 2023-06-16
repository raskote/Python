# Задание:
# https://i.gyazo.com/c9e59106c91a609ae261c02551eb8b4a.png

# Решение:
def make_header(s: str, d: int = 1):
    return "<h"+str(d)+">"+s+"</h"+str(d)+">"

print(make_header("Нет"))