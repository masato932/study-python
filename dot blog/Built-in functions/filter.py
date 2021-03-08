# words = ['Python', 'CSS', 'HTML', 'JavaScript', "march0308"]

# def text_len(word):
#     if len(word) > 7:
#         return True
#     else:
#         return False
    
# x = filter(text_len, words)

# for text in x:
#     print(text)

a = ['Python', 'CSS', 'HTML', 'JavaScript']

def y(z):
    if len(z) > 5:
        return True
    else:
        return False
    
x = list(filter(y, a))

print(x)
print(type(x))

# words = ['Python', 'CSS', 'HTML', 'JavaScript']

# x = filter(lambda word:True if len(word) > 5 else False, words)

# print(next(x))
# print(next(x))