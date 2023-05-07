# Задача:
# https://i.gyazo.com/375e34020d90cfd43886b37955f09db4.png

# Решение:
from string import ascii_lowercase
alphabet = {a: ord(a)-96 for a in ascii_lowercase}
print(alphabet)