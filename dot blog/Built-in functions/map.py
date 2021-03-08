words = ['Python', 'CSS', 'HTML', 'JavaScript']

def text_lower(word):
    return word.lower()
    
x = map(text_lower, words)

for text in x:
    print(text)

words = ['Python', 'CSS', 'HTML', 'JavaScript']

x = map(lambda word:word.lower(), words)

print(next(x))
print(next(x))
print(next(x))
print(next(x))