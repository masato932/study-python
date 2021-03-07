# words = ['Python', 'CSS', 'HTML', 'JavaScript']
    
# def word_edit(word_list, func):
#     new_words = []
#     for word in word_list:
#         new_word = func(word)
#         new_words.append(new_word)
        
#     return new_words
    
# def word_lower(word):
#     return word.lower()
    
# def word_upper(word):
#     return word.upper()

# print(word_edit(words, word_lower))

# print(word_edit(words, word_upper))

words = ['Python', 'CSS', 'HTML', 'JavaScript']
    
def word_edit(word_list, func):
    new_words = []
    for word in word_list:
        new_word = func(word)
        new_words.append(new_word)
        
    return new_words

print(word_edit(words, lambda word:word[0:3].lower()))

print(word_edit(words, lambda word:word[0:2].upper()))