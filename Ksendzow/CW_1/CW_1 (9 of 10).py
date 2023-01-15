# 9. Напишите функцию, которая принимает строки.
# Она должна вернуть False, если в строке содержится две одинаковые буквы,
# а если таких слов нет — True.

# no_duplicate_letters("Здравствуйте, Александра") ➞ False
# Две в в «Здравствуйте», три a в «Александра».

# no_duplicate_letters("Всегда дожимай до конца") ➞ True
# Две в в «Здравствуйте», три a в «Александра».

#Решение (not mine):
def foo(string):
        return len(set(string)) == len(string)

print(foo('test'))
print(foo('tes'))