# words = ['Python', 'CSS', 'HTML', 'JavaScript']

# iter_words = iter(words)

# print(type(words))
# print(type(iter_words))

# print(words)
# print(iter_words)

words = ['Python', 'CSS', 'HTML', 'JavaScript']

iter_words = iter(words)

print(next(iter_words))

print('######## iterator roop1 start #######')
for text in iter_words:
    print(text)

print('######## iterator roop2 start #######')
for text in words:
    print(text)