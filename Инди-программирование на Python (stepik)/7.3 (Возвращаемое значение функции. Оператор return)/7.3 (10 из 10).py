# Задание:
# https://i.gyazo.com/9459999f197827aa392c23d222422371.png


# Решение:
def count_AGTC(dna):
    li = [0, 0, 0, 0]
    if dna.count("A"):
        li[0] = dna.count("A")
    if dna.count("G"):
        li[1] = dna.count("G")
    if dna.count("T"):
        li[2] = dna.count("T")
    if dna.count("C"):
        li[3] = dna.count("C")
    return tuple(li)

# Альтернатива (not mine):
# def count_AGTC(dna):
#     return dna.count('A'), dna.count('G'), dna.count('T'), dna.count('C')


# код ниже не стоит удалять, он нужен для проверки
assert count_AGTC('AGGTC') == (1, 2, 1, 1)
assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
assert count_AGTC('CCT') == (0, 0, 1, 2)
print('Проверки пройдены')