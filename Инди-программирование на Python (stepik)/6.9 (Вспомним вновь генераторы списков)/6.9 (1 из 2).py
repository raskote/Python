# Задача:
# https://i.gyazo.com/2acc29662eea0b7daf950a13e641f616.png

# Решение:
colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']

print([(colors[i], sizes[j]) for i in range(len(colors)) for j in range(len(sizes))])


# Альтернатива (not mine):
# print([(c, s) for c in colors for s in sizes])

